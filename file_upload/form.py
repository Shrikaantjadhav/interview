from django import forms
from django.core.exceptions import ValidationError
from .models import UploadedFile
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ('file',)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email")

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30,
                            widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label='Password',
                            widget=forms.PasswordInput)