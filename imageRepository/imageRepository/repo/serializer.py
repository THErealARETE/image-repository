from rest_framework import serializers , validators
from .models import Images


from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)


class ImageSerializer(TaggitSerializer, serializers.ModelSerializer):
  """
  serializer for image object
  """

  tags = TagListSerializerField()
    
  class Meta:

    model = Images
    fields = '__all__'