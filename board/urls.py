from django.urls import path

from board.views import base_views, question_views

app_name = 'board'

urlpatterns = [
    path('', base_views.index, name='index'),
    path('<int:question_id>/', base_views.detail, name='detail'),
    path('<str:college>', question_views.question_college_list, name='question_college_list')
]