from django.urls import path

from trade import views

app_name = 'trade'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.PostCreate.as_view(), name='create_post'),
    path('detail/<int:pk>/', views.PostDetail.as_view(), name='detail'),
    path('update/<int:pk>/', views.PostUpdate.as_view(), name='update_post'),
    path('delete/<int:pk>/', views.PostDelete, name='delete_post'),

    path('detail/<int:pk>/new_comment/', views.new_comment, name='create_comment'),
    path('update_comment/<int:pk>/', views.CommentUpdate.as_view(), name='update_comment'),
    path('delete_comment/<int:pk>/', views.CommentDelete, name='delete_comment'),

]
