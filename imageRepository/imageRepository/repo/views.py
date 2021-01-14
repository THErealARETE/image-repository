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
        print([data['tags']])
        look = json.dumps([data['tags']])
        print(look)

        # tags_type = type(data("tags"))
        new_image_data = dict(
            image = data['image'],  
            title = data['title'],
            is_public = data['public'],
            # tags = ["tag1", "tag2"]
            tags = look
            # tags = data["tags"].replace(" ' ", " " ")
            # tags = ['tag': str(["xyz"]).replace("'", '"')]
        )   
        print(new_image_data)

        serializer = ImageSerializer(data = new_image_data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def list(self , request):
        queryset = Images.objects.all()
        serializer = ImageSerializer(queryset , many = True)
        return Response( serializer.data , status = status.HTTP_200_OK )


    def retrieve(self, request, pk = None):
        queryset = Images.objects.all()
        single_image = get_object_or_404(queryset, pk = pk )
        serializer = ImageSerializer(single_image)
        return Response(serializer.data, 
        status = status.HTTP_200_OK)


    # def update(self, request, *args, *kwargs):
    #     queryset = Images.objects.all()
    #     data = request.data 

    #     update_info = Images.objects.get()

    # def partial_update(self, request, pk = None):
    #     queryset = Images.objects.all()
    #     data = request.data
    #     print(data)
    #     image_to_update = get_object_or_404(queryset , pk = pk)
    #     print(image_to_update)


    #     serializer = ImageSerializer(image_to_update, data , partial = True)
    #     print(serializer.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data , status = status.HTTP_200_OK)
    #     return Response( serializer.errors , status=status.HTTP_400_BAD_REQUEST)    
        # updated_image = serializer.data
        # # updated_image = serializer(image_to_update).data
        # return Response( updated_image , status=status.HTTP_200_OK)
    
