from django.urls import path

from board.views import base_views, question_views, comment_views

app_name = 'board'

urlpatterns = [
    ## base_board
    path('<int:question_id>/', base_views.detail, name='detail'),
    path('create_comment/<int:question_id>/', comment_views.comment_create, name='comment_create'),

    ## question_views
    path('', question_views.question_college_list, name='index'),
    path('like/<int:question_id>/', question_views.question_like, name='question_like'),
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),
]