# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from photos.settings import LICENSES
from photos.validators import badwords_detector

PUBLIC='PUB'
PRIVATE='PRI'

VISIBILITY=(
    (PUBLIC,'Pública'),
    (PRIVATE,'Privada')
)


# Create your models here.
class Photo(models.Model):
    owner=models.ForeignKey(User)
    name=models.CharField(max_length=150)
    url=models.URLField()
    description=models.TextField(blank=True,null=True,default="",validators=[badwords_detector])
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    licence=models.CharField(max_length=3,choices=LICENSES)
    visibility=models.CharField(max_length=3,choices=VISIBILITY,default=PUBLIC)

    def __unicode__(self): #no params method
        return self.name

