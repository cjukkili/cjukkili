from django.urls import path

from board.views import base_views, question_views, answer_views

app_name = 'board'

urlpatterns = [
    path('', base_views.index, name='index'),
    path('<int:question_id>/', base_views.detail, name='detail'),
    path('<str:college>', question_views.question_college_list, name='question_college_list'),
    path('create_comment/<int:question_id>/', answer_views.comment_create, name='comment_create'),
    path('like/<int:question_id>/', question_views.question_like, name='question_like'),
]