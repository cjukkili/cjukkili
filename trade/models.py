from django.db import models

# Create your models here.
from common.models import User


class TradePost(models.Model):
    title = models.CharField(max_length=100)  # 글 제목
    content = models.TextField()  # 제품 설명
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 글쓴이
    price = models.IntegerField()  # 가격
    product_status = models.CharField(max_length=20)  # 제품 상태
    payment = models.CharField(max_length=20)  # 결제 방법
    shipping = models.CharField(max_length=20)  # 배송 방법
    create_date = models.DateTimeField(auto_now_add=True)  # 생성일
    modify_date = models.DateTimeField(auto_now=True)  # 수정일
    image = models.ImageField(upload_to='trade/%y/%m/%d', null=False)  # 상품 이미지

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/trade/detail/{self.pk}/'

class TradeComment(models.Model):
    post = models.ForeignKey(TradePost, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}'
