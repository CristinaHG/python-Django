from django import forms

from photos.models import Photo


class PhotoForm(forms.ModelForm):
    """formulario para el modelo Photo"""
    class Meta:
        model=Photo
        exclude=['owner']