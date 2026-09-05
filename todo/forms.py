from django import forms

from todo.models import Task


class TaskForm(forms.ModelForm):
    """Shared form for both creating and editing a task."""

    # Overridden so the HTML "datetime-local" picker parses correctly
    due_at = forms.DateTimeField(
        required=False,
        input_formats=["%Y-%m-%dT%H:%M"],
        widget=forms.DateTimeInput(
            attrs={"class": "form-control", "type": "datetime-local"},
            format="%Y-%m-%dT%H:%M",
        ),
    )

    class Meta:
        model = Task
        fields = [
            "title", "description", "classification", "status", "priority",
            "due_at", "related_link", "attachment", "repeat_label",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "classification": forms.Select(attrs={"class": "form-select"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "priority": forms.Select(attrs={"class": "form-select"}),
            "related_link": forms.URLInput(attrs={"class": "form-control"}),
            "attachment": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "repeat_label": forms.Select(attrs={"class": "form-select"}),
        }