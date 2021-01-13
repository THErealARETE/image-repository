from django.db import models

# Create your models here.

from taggit.managers import TaggableManager

class Images(models.Model):
    image_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to = 'image_bank',verbose_name= 'image')
    title = models.CharField(max_length= 250, verbose_name= 'image title/description')
    is_public = models.BooleanField(default= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = TaggableManager(blank= True , help_text= 'Add tags to your images' )

    