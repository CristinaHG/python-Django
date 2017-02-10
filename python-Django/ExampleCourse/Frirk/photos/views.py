from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
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
        return HttpResponseNotFound() # 404 nto found



