"""cjukkili URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings

from common.views import base_views

urlpatterns = [
    path('', base_views.index, name='index'),
    path('admin/', admin.site.urls),
    path('college/', include('board.urls')),
    path('common/', include('common.urls')),
    path('free/', include('free.urls')),
    path('accounts/', include('allauth.urls')),
    path('mypage/', include('mypage.urls')),
    path('club/', include('club.urls')),
    path('trade/', include('trade.urls')),
    path('contest/', include('contest.urls')),
    path('book/', include('book.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
