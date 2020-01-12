"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth import views as auth_views
from mysite.views import curdt, index, hours_ahead, dis_meta

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^date/$', curdt),
    path('time/',curdt),
    re_path(r'^time/plus/(\d{1,2})/$', hours_ahead),
    re_path(r'^req/$', dis_meta),
    path('',index),
]
