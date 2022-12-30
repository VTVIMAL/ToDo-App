from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.
class Task(models.Model):
    '''initialising fiels for the database'''
    title = models.CharField(max_length=100)
    discription = models.TextField(null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("task_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
