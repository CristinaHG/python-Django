# -*- coding=utf-8 -*-
from photos.settings import BADWORDS
from django.core.exceptions import ValidationError

def badwords_detector(value):
    """
    valida si en 'value' se han puesto tacos definidos en settings BADWORDS
    :return:boolean
    """

    for badword in BADWORDS:
        if badword.lower() in value.lower():
            raise ValidationError(u'La palabra {0} no está permitida'.format(badword))

    #si todo va ok devuelvo datos limpios
    return True