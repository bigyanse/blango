from django.contrib.auth import forms

from accounts.models import User

class UserCreationForm(forms.UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email") # password is required by default

class UserChangeForm(forms.UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "email") # password is required by default
