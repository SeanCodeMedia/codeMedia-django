# Create your models here.
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Category(models.Model):

    title           = models.CharField(max_length=100,default="")
    overview        = models.CharField(max_length=100,default="")
    coverImage      = models.ImageField(upload_to="uploads/categories")
    def __str__(self):
        return self.title


class BlogPost(models.Model):
    author          = models.CharField(default="Sean Peart", max_length=50)
    author_photo    = models.ImageField(upload_to="uploads/author_photos", default="")
    published       = models.DateTimeField(default=timezone.now)
    title           = models.CharField(max_length=100)
    overview        = models.TextField(max_length=100)
    body            = RichTextUploadingField(blank=True,null=True)
    body_2          = RichTextUploadingField(blank=True,null=True)
    main_coverImage = models.ImageField(upload_to="uploads/blogImages", default="")
    category        = models.ForeignKey(Category, default="", on_delete=models.CASCADE) # have to look into this cascade thing 

    def __str__(self):
        return self.title
