from django.contrib.auth.models import AbstractUser, User
from django.db import models


class College(models.Model):
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.department


class Gender(models.Model):
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.gender


class User(AbstractUser):
    gender = models.ForeignKey(Gender, null=True, on_delete=models.SET_NULL, default=3)
    college = models.ForeignKey(College, null=True, on_delete=models.SET_NULL, default=10)
    nickname = models.CharField(max_length=100, blank=False, null=False)
    profile_img = models.ImageField(upload_to='profile_img/', null=True, blank=True, default='/profile_img/default_profile_img.jpg')

    def get_college(self):
        return self.college


class Calendar(models.Model):
    content = models.CharField(max_length=100)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)

    def __str__(self):
        return self.content