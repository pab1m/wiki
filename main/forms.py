from django.contrib.auth.models import User

from .models import Authors
from django.forms import ModelForm, TextInput, Textarea, ImageField, ClearableFileInput
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

class AuthorsForm(ModelForm):
    class Meta:
        model = Authors
        fields = ['title', 'bio', 'photo']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть ПІБ',
            }),
            'bio': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть біографію',
            }),
            'photo': ClearableFileInput(attrs={
                'class': 'bd-placeholder-img bd-placeholder-img-lg featurette-image img-fluid mx-auto',
                'width': "100%",
                'height': "100%",
            }),
        }


class AuthUserForm(AuthenticationForm, LoginView, ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть ПІБ',
            }),
            'password': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть біографію',
            }),
        }