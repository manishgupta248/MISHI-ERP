from rest_framework import permissions, viewsets

from todo.models import Task
from todo.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    API for tasks — the entry point a future Telegram bot (or any other
    client) will use. Always scoped to the logged-in/authenticated user.
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)