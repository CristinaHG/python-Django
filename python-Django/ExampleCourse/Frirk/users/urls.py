# -*- coding=utf-8 -*-

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
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from users.api import UserViewSet

#APIRouter
router=DefaultRouter()
router.register(r'api/1.0/users',UserViewSet,base_name='user') #register users url


urlpatterns = [
    #Photos API URLs
    url(r'' ,include(router.urls)), #incluyo urls de API (photos y users porqe van a través del router)
]
