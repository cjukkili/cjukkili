from django import forms
from contest.models import Contest


class ContestForm(forms.ModelForm):
    class Meta:
        model = Contest  # 사용할 모델
        fields = ['name', 'registration_start_date', 'registration_end_date', 'contest_start_date', 'contest_end_date',
                  'site_url']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'registration_start_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
            'registration_end_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
            'contest_start_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
            'contest_end_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
            'site_url': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': '대회명',
            'registration_start_date': '모집 시작일',
            'registration_end_date': '모집 마감일',
            'contest_start_date': '대회 시작일',
            'contest_end_date': '대회 종료일',
            'site_url': '대회사이트 주소',
        }