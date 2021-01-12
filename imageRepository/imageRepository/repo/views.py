from django.shortcuts import render

# Create your views here.

from datetime import datetime, timedelta

from django.shortcuts import get_object_or_404

from rest_framework.response import Response

from rest_framework import viewsets,exceptions

from rest_framework.views import status

from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import action


from .serializer import ImageSerializer

from .models import Images

import json 


class ImageViewSet(viewsets.ModelViewSet):
    """
    POST image/
    GET image/
    GET image/:pk/
    PUT image/:pk/
    DELETE image/:pk/
    """


    serializer_class = Images
    queryset = Images.objects.all()

    def create(self, request):
        data = request.data 

        print(data)
        # j_data = json.dumps(data.tags)
        # print(j_data)
        new_image_data = dict(
            image = data['image'],  
            title = data['title'],
            is_public = data['public'],
            tags = json.dumps(data['tags'])
        )
        print(new_image_data)

        serializer = ImageSerializer(data = new_image_data)
        if serializer.is_valid():
            obj = serializer.save(commit = False)
            obj.save()
            serializer.save_m2m()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)