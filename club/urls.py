from django.urls import path

from club.views import base_views, question_views, comment_views

app_name = 'club'

urlpatterns = [
    path('', question_views.question_college_list, name='index'),
    path('<int:question_id>/', base_views.detail, name='detail'),

    path('create_comment/<int:question_id>/', comment_views.comment_create, name='comment_create'),
    path('update_comment/<int:pk>/', comment_views.CommentUpdate.as_view(), name='comment_update'),
    path('delete_comment/<int:comment_id>/', comment_views.comment_delete, name='comment_delete'),

    # question_views
    path('like/<int:question_id>/', question_views.question_like, name='question_like'),
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),
]