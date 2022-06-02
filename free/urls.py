from django.urls import path

from .views import base_views

app_name = 'free'

urlpatterns = [
    path('', base_views.index, name='index'),

]