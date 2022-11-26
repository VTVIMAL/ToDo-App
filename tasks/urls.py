from django.urls import path

from .views import TaskLists, TaskDetail, TaskCreate, TaskUpdate, TaskDelete

urlpatterns = [
    path("<int:pk>/", TaskDetail.as_view(), name="task_detail"),
    path("<int:pk>/edit/", TaskUpdate.as_view(), name="update"),
    path("<int:pk>/delete/", TaskDelete.as_view(), name="delete"),
    path("new/", TaskCreate.as_view(), name="new_task"),
    path("", TaskLists.as_view(), name="home"),
]