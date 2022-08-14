from django.db import models
from user.models import CustomUser


class Task(models.Model):
    priorities = (('low', 'Low'),
                  ('high', 'High'),
                  ('medium', 'Medium'))

    statuses = (('todo', 'To do'),
                ('in_progress', 'In progress'),
                ('blocked', 'Blocked'),
                ('finished', 'Finished'))

    name = models.CharField(max_length=100)
    text = models.TextField()
    deadline = models.DateTimeField()
    status = models.CharField(max_length=20, default=priorities[0][1], choices=statuses)
    priority = models.CharField(max_length=20, default=priorities[2][1], choices=priorities)
    importance = models.BooleanField(default=False, null=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank='true', null='true')
    date_created = models.DateTimeField(auto_now_add=True)
    # total_time = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tasks'
