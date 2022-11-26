from django.views.generic import CreateView, UpdateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render

from .forms import CustomUserCreationForm, UserForm


# Create your views here.

class SignUp(CreateView):
   form_class = CustomUserCreationForm
   success_url = reverse_lazy("login")
   template_name = "registration/signup.html"


# created a function based view for the profile page view
def userpage(request):
   if request.method == "POST":
      user_form = UserForm(request.POST, instance=request.user)
      if user_form.is_valid:
         user_form.save()
         messages.success(request,("Your profle was saved succesfully"))
   user_form = UserForm(instance = request.user)
   return render(request=request, template_name="profile.html", context={"user": request.user, "user_form":user_form })

