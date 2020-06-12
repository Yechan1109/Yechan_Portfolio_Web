from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.forms import EmailField


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('name','email')


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}))