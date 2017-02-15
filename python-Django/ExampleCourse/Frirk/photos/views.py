# -*- coding=utf-8 -*-
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.db.models import Q
# Create your views here.
from photos.forms import PhotoForm
from photos.models import Photo,PUBLIC


class PhotosQuerySet(object):

    def get_photos_queryset(self,request):
        if not request.user.is_authenticated(): # si no está autnticado
            photos=Photo.objects.filter(visibility=PUBLIC)
        elif request.user.is_superuser: # si es admin
            photos=Photo.objects.all()
        else:
            #photos=Photo.objects.filter(owner=request.user,visibility=PUBLIC)
            photos=Photo.objects.filter(Q(owner=request.user) | Q(visibility=PUBLIC))
        return photos #no es un array de fotos, es un objeto con la query configurada

class HomeView(View):

    def get(self,request):
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

class DetailView(View,PhotosQuerySet):

    def get(self,request,pk):
        possible_photos=self.get_photos_queryset(request).filter(pk=pk).select_related('owner')
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


class CreateView(View):
    @method_decorator(login_required())
    def get(self,request):
        """
        muestra un form para crear una foto
         :param request: HttpRequest
         :return: HttpResponse
        """

        form=PhotoForm()
        context={
            'form':form,
            'success_message': ''
        }

        return render(request,'photos/new_photo.html',context)


    @method_decorator(login_required())
    def post(self,request):
        """
         crea una foto en base a la información POST
         :param request: HttpRequest
         :return: HttpResponse
        """

        success_message=''

        photo_with_owner=Photo()
        photo_with_owner.owner=request.user #asigno como propietario de la foto al usuario atuenticado
        form=PhotoForm(request.POST,instance=photo_with_owner) #especificar instancia de foto a utilizar por el formulario
        if form.is_valid():
            new_photo=form.save() #guarda el objeto Photo y me lo devuelves
            form=PhotoForm()
            success_message='¡Guardado con éxito!'
            success_message+='<a href="{0}">'.format(reverse('photo_detail',args=[new_photo.pk]))
            success_message+='Ver foto'
            success_message+='</a>'
        context={
            'form':form,
            'success_message': success_message
        }

        return render(request,'photos/new_photo.html',context)


class ListView(View,PhotosQuerySet):

    def get(self,request):

        """
        Devuelve:
        - las fotos publicas si el usuario no está autenticado,
        - las fotos del usuario autenticado o las publicas de otros
        - si el usuario es superadmin,devuelve todas las fotos
        :param request: HttpRequest
        :return: HttpResponse
        """

        context={
            'photos':self.get_photos_queryset(request)
        }

        return render(request,'photos/photos_list.html',context)









