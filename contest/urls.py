from django.urls import path

from contest import views

app_name = 'contest'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.ContestCreate.as_view(), name='create_contest'),
    path('detail/<int:pk>/', views.ContestDetail.as_view(), name='detail'),
    path('update/<int:pk>/', views.ContestUpdate.as_view(), name='update_contest'),
    path('delete/<int:pk>/', views.ContestDelete, name='delete_contest'),

]
