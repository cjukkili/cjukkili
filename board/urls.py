from django.urls import path

from board.views import base_views, question_views, answer_views

app_name = 'board'

urlpatterns = [
    path('', question_views.question_college_list, name='index'),
    path('<int:question_id>/', base_views.detail, name='detail'),
    # path('<str:college>', question_views.question_college_list, name='question_college_list'),
    path('create_comment/<int:question_id>/', answer_views.comment_create, name='comment_create'),
    path('like/<int:question_id>/', question_views.question_like, name='question_like'),
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),
]