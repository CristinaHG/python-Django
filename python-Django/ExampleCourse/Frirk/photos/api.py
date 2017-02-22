# -*- coding= utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response
from photos.models import Photo
from photos.serializers import PhotoSerializer, PhotoListSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# class PhotoListAPI(APIView):
#
#     def get(self,request):
#         photos=Photo.objects.all()
#         serializer=PhotoSerializer(photos,many=True)
#         return Response(serializer.data)
from photos.views import PhotosQuerySet


class PhotoListAPI(PhotosQuerySet,ListCreateAPIView):
    queryset = Photo.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    #serializer_class = PhotoListSerializer

    def get_serializer_class(self):
        return PhotoSerializer if self.request.method=="POST" else PhotoListSerializer

    def get_queryset(self):
        return self.get_photos_queryset(self.request)




class PhotoDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

