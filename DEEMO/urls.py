"""DEEMO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf.urls import url
from django.conf import settings
from djoser import views
from djoser.urls import authtoken

urlpatterns = []

if settings.ADMIN_ENABLED is True:
    urlpatterns += [path('admin/', admin.site.urls),]

if settings.LOGIN_PROVIDED is True:
    urlpatterns += [re_path(r'^api/auth/token/login/?$', views.TokenCreateView.as_view(), name="login"),]

urlpatterns += [
    path('', include('api.urls')),
    re_path(r'^api/auth/token/logout/?$', views.TokenDestroyView.as_view(), name="logout"),
    #url(r'^api/auth/', include('djoser.urls')),
]
