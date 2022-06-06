from django import forms
from django.contrib.auth.forms import UserCreationForm

from common.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    username = forms.CharField(label="아이디")

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "password1", "password2",
                  "nickname", "email", "gender", "college")