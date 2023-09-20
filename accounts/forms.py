from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms


attrs = {'class': 'form-control'}



class UserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs=attrs)
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs=attrs)
    )



class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(attrs=attrs)
    )

    last_name = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(attrs=attrs)
    )

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs=attrs)
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs=attrs)
    )

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs=attrs)
    )

    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput(attrs=attrs)
    )
    #HamzawaleedNasr123$
    class Meta(UserCreationForm.Meta):
        model = Profile
        fields = UserCreationForm.Meta.fields + ("profile_image","status")


    field_order = ['first_name', 'last_name', 'username', 'profile_image', 'email', 'password1', 'password2', 'status']    