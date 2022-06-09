from django import forms
from board.models import Comment, Question


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question  # 사용할 모델
        fields = ['title', 'college', 'content', 'imgs']
        field_classes = {

        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'college': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': '제목',
            'content': '내용',
            'college': '단과대학',
            'imgs': '이미지',
        }