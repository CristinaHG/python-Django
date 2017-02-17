# -*- coding=utf-8 -*-
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password as validate_password_django
class UserSerializer(serializers.Serializer):

    id=serializers.ReadOnlyField() #read only field
    first_name=serializers.CharField()
    last_name=serializers.CharField()
    username=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()


    def create(self, validated_data):
        """
        Crea una instancia de User a partirr de los datos de validated_data que contiene
        valores deserializados
        :param validated_data: Diccionario con datos de usuario
        :return: objeto User
        """

        instance=User()
        return self.update(instance,validated_data)


    def update(self, instance, validated_data):
        """
        Actualiza una instancia de User a partir de los datos
        del diccionario validated_data que contiene valores deserializados
        :param instance: objeto User a actualizar
        :param validated_data: diccionario con nuevos vallores para el User
        :return: objeto User actualizado
        """
        instance.first_name=validated_data.get('first_name')
        instance.last_name=validated_data.get('last_name')
        instance.username=validated_data.get('username')
        instance.email=validated_data.get('email')
        instance.set_password(validated_data.get('password'))
        instance.save()

        return instance


    def validate_username(self, data):
        """
        valida si existe un usuario con ese username
        :param data:
        :return:
        """
        users=User.objects.filter(username=data)

        # Si estoy creando( no hay instancia), comprobar si hay usuarios con ese username
        if not self.instance and len(users)!=0:
            raise serializers.ValidationError("Ya existe un usuario con ese username")
        #si estoy actualizando, el nuevo username es diferente al de la instancia(está cambiando el username)
        # y existen usuarios ya registrados con el nuevo username
        elif  self.instance and self.instance.username !=data and len(users)!=0:
            raise serializers.ValidationError("Ya existe un usuario con ese username")

        else:
            return data


    def validate_password(self, data):
        """
        valida que la contraseña cumpla una seguridad minima
        :param data:
        :return:
        """
        validate_password_django(data)
