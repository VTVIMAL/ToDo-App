from django.urls import path

from .views import SignUp, userpage

urlpatterns = [
    path("signup/", SignUp.as_view(), name="signup"),
    path("user/", userpage, name="profile"), # endpoint for the user profile
]
