"""frikr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import photos
from photos import views


urlpatterns = [
    #photos urls
    url(r'^admin/', admin.site.urls),
    url(r'^$', photos.views.home,name='photos_home'),
    url(r'^photos/(?P<pk>[0-9]+)$',photos.views.detail,name='photo_detail'),
    #users urls
    url(r'^login$','users.views.login',name='users_login'),
    url(r'^logout$','users.views.logout',name='users_logout')
]


