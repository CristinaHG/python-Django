# -*- coding= utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response
from photos.models import Photo
from photos.serializers import PhotoSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

# class PhotoListAPI(APIView):
#
#     def get(self,request):
#         photos=Photo.objects.all()
#         serializer=PhotoSerializer(photos,many=True)
#         return Response(serializer.data)

class PhotoListAPI(ListCreateAPIView):

    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class PhotoDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

