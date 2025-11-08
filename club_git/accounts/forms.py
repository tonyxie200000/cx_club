# accounts/forms.py

from django import forms
from django.contrib.auth.models import User  # 使用内置的User模型
from django.contrib.auth.forms import UserCreationForm  # 可选：用于注册的表单


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '用户名或邮箱'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '密码'}))
