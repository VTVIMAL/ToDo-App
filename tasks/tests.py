from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
# Create your tests here.

from .models import Task

class TaskModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):

        cls.user = get_user_model().objects.create_user(
            username = "testuser",
            email = "testuser@email.com",
            password = "testing123"
        )
        
        cls.task = Task.objects.create(
            title = "Task title",
            discription = "Task content",
            author = cls.user
        )

    def test_task_list(self):
        self.assertEqual(f"{self.task.title}", "Task title")
        self.assertEqual(f"{self.task.discription}", "Task content")
        

    def test_task_list_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Task title")
        self.assertTemplateUsed(response, "task_list.html")

    def test_task_detail_view(self):
        response = self.client.get(self.task.get_absolute_url())
        no_response = self.client.get("/1234/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Task title")
        self.assertContains(response, "Task content")
        self.assertTemplateUsed(response, "task_detail.html")