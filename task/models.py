from django.db import models
from user.models import CustomUser


class Task(models.Model):
    priorities = (('l', 'low'),
                  ('h', 'high'),
                  ('m', 'medium'))

    statuses = (('t', 'todo'),
                ('ip', 'in_progress'),
                ('b', 'blocked'),
                ('f', 'finished'))

    name = models.CharField(max_length=100)
    text = models.TextField()
    deadline = models.DateField()
    status = models.CharField(max_length=20, default=priorities[0], choices=statuses)
    priority = models.CharField(max_length=20, default=priorities[2], choices=priorities)
    importance = models.BooleanField(default=False, null=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank='true', null='true')

    class Meta:
        db_table = 'tasks'
