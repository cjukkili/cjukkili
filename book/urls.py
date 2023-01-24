from django.urls import path

from book.views import base_views

app_name = 'book'

urlpatterns = [
    path('', base_views.index, name='index'),
]