from django import forms
from board.models import Comment, Question


class ClubQuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        fields = ['title', 'content', 'imgs']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'imgs': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'})
        }
        labels = {
            'title': '제목',
            'content': '내용',
            'imgs': '이미지',
        }