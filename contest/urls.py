from django.urls import path

from contest import views

app_name = 'contest'

urlpatterns = [
    path('', views.index, name='index'),

]
