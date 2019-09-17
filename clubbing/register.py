from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.edit import FormView
from django.views import View
from django.contrib.auth import login, authenticate
from clubbing.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Это поле обязательно')
    username = forms.CharField(min_length=3, max_length=20, help_text='Длина логина должна быть не меньше 3-х и не больше 20')
    class Meta:
        model = User
        fields = ('username', 'email', 'group', 'password1', 'password2', )