# -*- coding=utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError

from photos.models import Photo
from photos.settings import BADWORDS


class PhotoForm(forms.ModelForm):
    """formulario para el modelo Photo"""
    class Meta:
        model=Photo
        exclude=['owner']


    def clean(self):
        """
        valida si en la descripción se han puesto tacos definidos en settings BADWORDS
        :return: diccionario con los atributos
        """

        cleaned_data=super(PhotoForm,self).clean()

        description=cleaned_data.get('description','')

        for badword in BADWORDS:
            if badword.lower() in description:
                raise ValidationError(u'La palabra {0} no está permitida'.format(badword))


        #si todo va ok devuelvo datos limpios
        return cleaned_data