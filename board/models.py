from common.models import User, College
from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.category_name


class BoardType(models.Model):
    target = models.CharField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.target


class Question(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='author_question', to_field='id')
    # nickname = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='nickname_question', to_field="nickname")
    board_type = models.ForeignKey(BoardType, null=True, on_delete=models.CASCADE, to_field='id')
    college = models.ForeignKey(College, null=True, on_delete=models.CASCADE, blank=True, to_field='id')
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, to_field='category_name')
    like = models.ManyToManyField(User, blank=True, related_name='like_question')
    imgs = models.ImageField(upload_to="%y/%m/%d", null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.board_type.target}/{self.id}/'


class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return self.question.get_absolute_url()

