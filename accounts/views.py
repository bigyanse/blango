from django.urls import reverse_lazy
from django.views import generic

from accounts.forms import UserCreationForm

class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "register.html"
