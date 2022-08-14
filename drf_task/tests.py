from rest_framework.test import APITestCase
from task.models import Task
from user.models import CustomUser


class TaskTests(APITestCase):
    def setUp(self):
        user = CustomUser.objects.create_user(email='test_user@gmail.com', password='ALkj23hbd2')
        user.save()

        self.one_task = Task.objects.create(
            name='TestTask',
            text='TestTaskTestTaskTestTask...TestTaskTestTask',
            user=user
        )
