from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User1


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


class UserRegisterForm(UserCreationForm):

    profile_image = forms.ImageField(
        label="Choose your profile photo (optional)",
        required=False
    )

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

    status = forms.Select()

    class Meta(UserCreationForm.Meta):
        model = User1
        fields = UserCreationForm.Meta.fields + ("profile_image","status",)   