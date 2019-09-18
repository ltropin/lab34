from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.edit import FormView
from django.views import View
from django import forms
from django.contrib.auth import login, authenticate
from clubbing.models import User, Purchase, Item, Order


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=255,
                             required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}),
                             help_text='Это поле обязательно')
    group = forms.ChoiceField(widget=forms.Select(attrs={'class': 'custom-select'}),
                              choices=User.GROUP_CHOICE,
                              label='Группа:')
    username = forms.CharField(min_length=3,
                               max_length=20,
                               help_text='Длина логина должна быть не меньше 3-х и не больше 20',
                               widget=forms.TextInput(attrs={'class': 'form-control'}),
                               label='Логин:')
    password1 = forms.CharField(min_length=6,
                               max_length=35,
                               help_text='Длина пароля должна быть не меньше 6 и не больше 35',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               label='Пароль:')
    password2 = forms.CharField(min_length=6,
                               max_length=35,
                               help_text='Длина пароля должна быть не меньше 6 и не больше 35',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               label='Повторите пароль:')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'group', 'password1', 'password2', )


class AddPurchase(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(),
                                  widget=forms.HiddenInput())

    item = forms.ModelChoiceField(queryset=Item.objects.all(),
                                  widget=forms.Select(attrs={'class': 'custom-select'}),
                                  required=True,
                                  label='Товар:')

    status = forms.ChoiceField(widget=forms.Select(attrs={'class': 'custom-select'}),
                               choices=Purchase.STATUS_CHOICE,
                               label='Статус:')

    max_cost = forms.IntegerField(max_value=999999999,
                                  min_value=100,
                                  widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                  label='Максимальная стоимость:')
    class Meta:
        model = Purchase
        fields = ['item', 'status', 'max_cost', 'user']


class FormOrder(forms.ModelForm):
    buyer = forms.ModelChoiceField(queryset=User.objects.all(),
                                   widget=forms.HiddenInput())
    purchase = forms.ModelChoiceField(queryset=Purchase.objects.all(),
                                   widget=forms.HiddenInput())
    class Meta:
        model = Order
        fields = ['purchase', 'buyer']
