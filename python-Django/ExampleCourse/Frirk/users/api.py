# -*- coding=utf-8 -*-
from django.contrib.auth.models import User
from django.views.generic import View
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

class UserListAPI(APIView):

    def get(self,request):
        #instancio paginador
        paginator=PageNumberPagination()
        users=User.objects.all() #devuelve un queryset
        #paginar el queryset
        paginator.paginate_queryset(users,request)
        serializer=UserSerializer(users,many=True)
        serialized_users=serializer.data #tomar usuarios serializados
        # renderer=JSONRenderer()
        # json_users=renderer.render(serialized_users) #lista de diccionarios-> JSON
        # return HttpResponse(json_users)

        #devolver respuesta paginada
        return paginator.get_paginated_response(serialized_users)

    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user=serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED) #optional
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPI(APIView):

    def get(self,request,pk):
        user=get_object_or_404(User,pk=pk) #si existe usuario con clave igual a pk lo devuelve,sino devuelve él un 404
        serializer=UserSerializer(user)
        return Response(serializer.data)


    def put(self,request,pk):
        user=get_object_or_404(User,pk=pk)
        serializer=UserSerializer(instance=user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk):
        user=get_object_or_404(User,pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
