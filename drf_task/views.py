from rest_framework.viewsets import ModelViewSet
from drf_task.serializers import TaskSerializer
from task.models import Task


class TaskGenericViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        print(self.request.user)
        if self.request.user.is_authenticated:
            serializer.save(**{'user': self.request.user})
        else:
            serializer.save()

    # def get_queryset(self):
    #     user = self.request.user
    #     return Task.objects.filter(user=user)
