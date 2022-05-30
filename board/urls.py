from django.urls import path

from board.views import base_views

app_name = 'board'

urlpatterns = [
    path('', base_views.index, name='index'),
]