from django.db import models


class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    author = models.TextField()
    publisher = models.TextField()
    pubMonth = models.TextField()
    price = models.TextField()
    info = models.TextField(null=True)
    index = models.TextField(null=True)