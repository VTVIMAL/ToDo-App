from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    '''Create a user creation / signup form using the custom user model'''
    class Meta:
        model = CustomUser
        fields = ("username", "email", ) # fields to be used


class CustomUserChangeForm(UserChangeForm):
    '''Create a user change form / modify user form using the custom user model'''
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields # use the same fields as the UserChangeForm
        # fields = ("username", "first_name", "last_name", "email")
    

class UserForm(forms.ModelForm):
    ''' From used for the userpage'''
    # used to update the below given fields
    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "last_name", "email")