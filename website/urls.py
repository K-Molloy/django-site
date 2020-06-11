"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from website.views import home

app_name = (
    'landing',
    'posts',
    'user_info',
    'newsletters',
    'kieran_portfolio'
)

urlpatterns = [

    # Basic URLS
    path('admin/', admin.site.urls, name='admin'),
    path('home/', home, name='home'),
    
    # App URLS
    path('', include('landing.urls'), name='landing'),
    path('posts/', include('posts.urls'), name='posts'),
    path('user-info/', include('user_info.urls'), name='users'),
    path('portfolio/', include('kieran_portfolio.urls'), name='portfolio'),
    path('newsletter/', include('newsletters.urls'), name='newsletter'),
    path('comments/', include('comments.urls'), name='comments'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


















