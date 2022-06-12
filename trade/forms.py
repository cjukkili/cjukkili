from django import forms
from django.db import models

from trade.models import TradePost, TradeComment


class PostForm(forms.ModelForm):
    class Meta:
        model = TradePost
        fields = ['title', 'price', 'product_status', 'payment', 'shipping','content',  'image']
        labels = {
            'title': '제목',
            'content': '내용',
            'price': '가격',
            'image': '이미지',
            'product_status': '제품 상태',
            'product_status': '결제 방식',
            'product_status': '배송 방법',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = TradeComment
        fields = ['content',]