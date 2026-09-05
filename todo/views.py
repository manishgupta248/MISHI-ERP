from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from todo.forms import TaskForm
from todo.models import Task

# Sort options allowed via ?sort= in the URL — kept as a whitelist for safety
ALLOWED_SORTS = {"due_at", "-due_at", "priority", "-priority", "title"}


class OwnerQuerysetMixin(LoginRequiredMixin):
    """Ensures a user only ever sees or edits their own tasks."""
    model = Task

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)


class TaskListView(OwnerQuerysetMixin, ListView):
    template_name = "todo/task_list.html"
    context_object_name = "tasks"
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()

        status = self.request.GET.get("status")
        classification = self.request.GET.get("classification")
        priority = self.request.GET.get("priority")
        sort = self.request.GET.get("sort", "-priority")

        if status:
            queryset = queryset.filter(status=status)
        if classification:
            queryset = queryset.filter(classification=classification)
        if priority:
            queryset = queryset.filter(priority=priority)

        if sort not in ALLOWED_SORTS:
            sort = "-priority"

        return queryset.order_by(sort)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["status_choices"] = Task.Status.choices
        context["classification_choices"] = Task.Classification.choices
        context["priority_choices"] = Task.Priority.choices
        context["current_status"] = self.request.GET.get("status", "")
        context["current_classification"] = self.request.GET.get("classification", "")
        context["current_priority"] = self.request.GET.get("priority", "")
        context["current_sort"] = self.request.GET.get("sort", "-priority")
        return context


class TaskCreateView(OwnerQuerysetMixin, CreateView):
    template_name = "todo/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("todo:task_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user  # attach task to the logged-in user
        return super().form_valid(form)


class TaskUpdateView(OwnerQuerysetMixin, UpdateView):
    template_name = "todo/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("todo:task_list")


class TaskDeleteView(OwnerQuerysetMixin, DeleteView):
    template_name = "todo/task_confirm_delete.html"
    success_url = reverse_lazy("todo:task_list")