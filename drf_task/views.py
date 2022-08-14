from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from drf_task.serializers import TaskSerializer
from task.models import Task
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from core import settings
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('status',)
    search_fields = ('name',)

    def create(self, request, *args, **kwargs):
        return super(TaskViewSet, self).create(request)

    def perform_create(self, serializer):
        serializer.save(**{'user': self.request.user})

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    @action(methods=['post'], detail=True)
    def do_importance(self, request, pk=None):
        task = self.get_object()
        task.importance = True
        task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def change_status(self, request, pk=None):
        task = self.get_object()
        ts = task.status
        if ts == 'todo':
            task.status = 'in_progress'
        elif ts == 'in_progress':
            task.status = 'finished'
        task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def status_blocked(self, request, pk=None):
        task = self.get_object()
        task.status = 'blocked'
        task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def priority_low(self, request, pk=None):
        task = self.get_object()
        task.priority = 'low'
        task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def priority_medium(self, request, pk=None):
        task = self.get_object()
        task.priority = 'medium'
        task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def priority_high(self, request, pk=None):
        task = self.get_object()
        task.priority = 'high'
        task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data)
