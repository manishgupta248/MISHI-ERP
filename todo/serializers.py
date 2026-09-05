from rest_framework import serializers

from todo.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id", "title", "description", "classification", "status",
            "priority", "due_at", "related_link", "attachment",
            "repeat_label", "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]