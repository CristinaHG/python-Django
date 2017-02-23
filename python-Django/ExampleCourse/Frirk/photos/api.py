# -*- coding= utf-8 -*-
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

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

class PhotoViewSet(PhotosQuerySet,ModelViewSet):

    queryset = Photo.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields=('name','description','owner__first_name')
    ordering_fields=('name','owner')


    def get_queryset(self):
        return self.get_photos_queryset(self.request)

    def get_serializer_class(self):
        if self.action=='list':
            return PhotoListSerializer
        else:
            return PhotoSerializer

    def perform_create(self, serializer):
        """
        Asigna automáticamente la autoría de ka nueva foto al
        usuario autenticado
        :param serializer:
        :return:
        """
        serializer.save(owner=self.request.user)

# class PhotoListAPI(PhotosQuerySet,ListCreateAPIView):
#     queryset = Photo.objects.all()
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#     #serializer_class = PhotoListSerializer
#
#     def get_serializer_class(self):
#         return PhotoSerializer if self.request.method=="POST" else PhotoListSerializer
#
#     def get_queryset(self):
#         return self.get_photos_queryset(self.request)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#
#
#
# class PhotoDetailAPI(PhotosQuerySet, RetrieveUpdateDestroyAPIView):
#     queryset = Photo.objects.all()
#     serializer_class = PhotoSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#
#     def get_queryset(self):
#         return self.get_photos_queryset(self.request)
#
