from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterUserForm

# Create your views here.

def profile(request):
    return render(
        request,
        'common/profile.html'
    )

class RegisterView(CreateView):
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'