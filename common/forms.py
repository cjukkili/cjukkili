from django import forms
from django.contrib.auth.forms import UserCreationForm

from common.models import User


class UserForm(UserCreationForm):
    password1 = forms.CharField(label='비밀번호', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='비밀번호(확인)', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password1", "password2",
                  "nickname", "email", "gender", "college", "profile_img"]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'nickname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'college': forms.Select(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'profile_img': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }
        labels = {
            'first_name': '성',
            'last_name': '이름',
            'username': '아이디',
            'nickname': '닉네임',
            'email': '이메일',
            'gender': '성별',
            'college': '단과대학',
            'profile_img': '프로필 사진',
        }