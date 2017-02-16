# -*- coding=utf-8 -*-
from django.contrib.auth.models import User
from django.views.generic import View
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
from django.shortcuts import get_object_or_404

class UserListAPI(APIView):

    def get(self,request):
        users=User.objects.all()
        serializer=UserSerializer(users,many=True)
        serialized_users=serializer.data #tomar usuarios serializados
        # renderer=JSONRenderer()
        # json_users=renderer.render(serialized_users) #lista de diccionarios-> JSON
        # return HttpResponse(json_users)
        return Response(serialized_users)

class UserDetailAPI(APIView):

    def get(self,request,pk):
        user=get_object_or_404(User,pk=pk) #si existe usuario con clave igual a pk lo devuelve,sino devuelve él un 404
        serializer=UserSerializer(user)
        return Response(serializer.data)