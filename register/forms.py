from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Users
from django.forms import ModelForm, TextInput, CharField, PasswordInput

class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ['user_name', 'email', 'password']

        widgets = {
            'user_name': TextInput(attrs={
                'class': 'form-control buff',
                'placeholder': "Ім'я"
            }),
            'password': TextInput(attrs={
                'class': 'form-control buff',
                'placeholder': 'Пароль'
            }),
            'email': TextInput(attrs={
                'class': 'form-control buff',
                'placeholder': 'Електронна адреса'
            })
        }

class RegisterUserForm(UserCreationForm):
    username = CharField(label="Ім'я", widget=TextInput(attrs={
        'class': 'form-control buff',
        'placeholder': "Ім'я"
    }))
    password1 = CharField(label='Пароль', widget=PasswordInput(attrs={
        'class': 'form-control buff',
        'placeholder': 'Пароль'
    }))
    password2 = CharField(label='Підтвердіть пароль', widget=PasswordInput(attrs={
        'class': 'form-control buff',
        'placeholder': 'Підтвердіть пароль'
    }))
    email = CharField(label='Електронна адреса', widget=TextInput(attrs={
        'class': 'form-control buff',
        'placeholder': 'Електронна адреса'
    }))

    class Meta:
        model = User

        fields = ('username', 'password1', 'password2', 'email')

        widgets = {
            'user_name': TextInput(attrs={
                'class': 'form-control buff',
                'placeholder': "Ім'я"
            }),
            'password1': PasswordInput(attrs={
                'class': 'form-control buff',
                'placeholder': 'Пароль'
            }),
            'password2': PasswordInput(attrs={
                'class': 'form-control buff',
                'placeholder': 'Підтвердіть пароль'
            }),
            'email': TextInput(attrs={
                'class': 'form-control buff',
                'placeholder': 'Електронна адреса'
            })
        }


class LoginUserForm(AuthenticationForm):

    username = CharField(label="Ім'я", widget=TextInput(attrs={
        'class': 'form-control buff',
        'placeholder': "Ім'я"
    }))
    password = CharField(label='Пароль', widget=PasswordInput(attrs={
        'class': 'form-control buff',
            'placeholder': 'Пароль'
    }))