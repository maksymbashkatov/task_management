from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient
from task.models import Task
from user.models import CustomUser


class TaskTests(APITestCase):
    def setUp(self):
        user = CustomUser.objects.create_user(email='test_user@gmail.com', password='ALkj23hbd2')
        user.save()

        self.user_token = Token.objects.get(user=user)

        self.data = {
            'name': 'TestTask',
            'text': 'TestTaskTestTaskTestTask...TestTaskTestTask',
            'deadline': '2022-08-16',
            'user': user
        }

    def test_create_valid_task(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user_token.key}')
        response = self.client.post(reverse('drf_all-list'), self.data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_tasks_list(self):
        response = self.client.get(reverse('drf_all-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
