from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.



class Category(models.Model):

	title 			= models.CharField(max_length=100)
	overview 		= models.CharField(max_length=100)
	coverImage		= models.ImageField(upload_to="uploads/categories", default="")

	def __str__(self):
		return self.title


class BlogPost(models.Model):
    id              = models.BigAutoField(primary_key=True)
    author 			= models.CharField(default="Sean Peart", max_length=50)
    author_photo 	= models.ImageField(upload_to="uploads/author_photos", default="uploads/author_photos/image1.jpg")
    published 		= models.DateTimeField(default=timezone.now)
    title 			= models.CharField(max_length=100)
    overview 		= models.TextField(max_length=100)
    body 			= RichTextUploadingField(blank=True,null=True)
    coverImage		= models.ImageField(upload_to="uploads/blogImages", default="")
    main_coverImage = models.ImageField(upload_to="uploads/blogImages", default="")
    category_id 	= models.ForeignKey(Category, default="", on_delete=models.CASCADE) # have to look into this cascade thing 

    def __str__(self):
    	return self.title




