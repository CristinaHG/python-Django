# -*- coding=utf-8 -*-
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):

    id=serializers.ReadOnlyField() #read only field
    first_name=serializers.CharField()
    last_name=serializers.CharField()
    username=serializers.CharField()
    email=serializers.CharField()
    password=serializers.CharField()


    def create(self, validated_data):
        """
        Crea una instancia de User a partirr de los datos de validated_data que contiene
        valores deserializados
        :param validated_data: Diccionario con datos de usuario
        :return: objeto User
        """

        instance=User()
        instance.first_name=validated_data.get('first_name')
        instance.last_name=validated_data.get('last_name')
        instance.username=validated_data.get('username')
        instance.email=validated_data.get('email')
        instance.set_password(validated_data.get('password'))
        instance.save()

        return instance


    