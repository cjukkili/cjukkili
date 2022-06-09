from django.urls import path
from .views import fquestion_views, comment_views
from .views import base_views

app_name = 'free'

urlpatterns = [
    path('<int:question_id>/', base_views.detail, name='detail'),


    path('create_comment/<int:question_id>/', comment_views.comment_create, name='comment_create'),

    # fquestion_view
    path('', fquestion_views.question_free_list, name='index'),
    path('like/<int:question_id>/', fquestion_views.question_like, name='question_like'),
    path('question/create/', fquestion_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', fquestion_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', fquestion_views.question_delete, name='question_delete'),
]