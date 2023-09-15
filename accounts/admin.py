from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from accounts.models import User
from accounts.forms import UserChangeForm, UserCreationForm

class UserAdmin(auth_admin.UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ["username", "is_staff", "is_superuser"]

admin.site.register(User, UserAdmin)
