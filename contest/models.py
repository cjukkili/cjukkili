from django.db import models


class Contest(models.Model):
    name = models.CharField(max_length=50)  # 대회명
    content = models.TextField()  # 대회 설명
    registration_start_date = models.DateTimeField()  # 접수 시작일
    registration_end_date = models.DateTimeField()  # 접수 종료일
    contest_start_date = models.DateTimeField()  # 대회 시작일
    contest_end_date = models.DateTimeField()  # 대회 종료일
    site_url = models.TextField()  # 대회 사이트 링크

    def __str__(self):
        return self.name