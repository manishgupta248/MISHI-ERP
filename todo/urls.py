from django.urls import path

from todo.views import TaskCreateView, TaskDeleteView, TaskListView, TaskUpdateView

app_name = "todo"

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("new/", TaskCreateView.as_view(), name="task_create"),
    path("<int:pk>/edit/", TaskUpdateView.as_view(), name="task_edit"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
]