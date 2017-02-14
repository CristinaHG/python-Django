# -*- coding=utf-8 -*-
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.core.urlresolvers import reverse

# Create your views here.
from photos.forms import PhotoForm
from photos.models import Photo,PUBLIC


def home(request):
    photos=Photo.objects.filter(visibility=PUBLIC).order_by('-created_at')
    # html='<ul>'
    # for photo in photos:
    #     html+='<li>'+photo.name+'</li>'
    # html+='</ul>'
    # return HttpResponse(html)
    context={
        'photos_list': photos[:5]
    }
    return render(request,'photos/home.html',context)

# loads detail page of photo
# receive request and photo identifier
def detail(request,pk):
    possible_photos=Photo.objects.filter(pk=pk)
    photo=possible_photos[0] if len(possible_photos)==1 else None
    #if photo exits, load template, else error
    if photo is not None:
        #load detail template
        context={
            'photo':photo
        }
        return render(request,'photos/detail.html',context)
    else:
        return HttpResponseNotFound('No existe la foto') # 404 nto found



def create(request):
    """
    muestra un form para crear una foto y la crea si la petición es post
     :param request: HttpRequest
     :return: HttpResponse
    """
    success_message=''

    if request.method=='GET':
        form=PhotoForm()
    else:
        form=PhotoForm(request.POST)
        if form.is_valid():
            new_photo=form.save() #guarda el objeto Photo y me lo devuelves
            form=PhotoForm()
            success_message='¡Guardado con éxito!'
            success_message+='<a href="'+ reverse('photo_detail',[new_photo.pk]) +'">'
            success_message+='Ver foto'
            success_message+='</a>'
    context={
        'form':form,
        'success_message': success_message
    }



    return render(request,'photos/new_photo.html',context)
