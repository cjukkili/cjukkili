from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class College(models.Model):
    department = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.department


class Gender(models.Model):
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.gender


class User(AbstractUser):
    gender = models.ForeignKey(Gender, null=True, on_delete=models.SET_NULL)
    college = models.ForeignKey(College, null=True, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100, unique=True)

    def get_college(self):
        return self.college


