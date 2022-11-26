from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm # form used for user creation
    form = CustomUserChangeForm # form used for user update
    list_display = [ # fields to be displayed at the admin page
        "email",
        "username",
        "is_staff",
    ]


admin.site.register(CustomUser, CustomUserAdmin)

