# -*- coding=utf-8 -*-

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
