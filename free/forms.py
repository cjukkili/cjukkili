from django import forms

from board.models import Question


class FreeQuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        fields = ['title', 'category', 'content', 'imgs']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'imgs': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'})
        }
        labels = {
            'title': '제목',
            'content': '내용',
            'category': '카테고리',
            'imgs': '이미지',
        }