from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Project(models.Model):

	title 				= models.CharField(max_length=100)
	short_description 	= RichTextUploadingField(blank=True,null=True)
	githubLlink 		= models.URLField(default="https://github.com/SeanCodeMedia")
	linkedinLlink 		= models.URLField(default="https://www.linkedin.com/in/seanpeart/")
	youtubeLink 		= models.URLField(default="https://www.youtube.com/channel/UC8qa9USnmzi-ewkXTMiZ9LA?view_as=subscriber")
	Icon 				= models.ImageField(upload_to="uploads/profile/project_photos", default="")
	project_photo1 		= models.ImageField(upload_to="uploads/profile/project_photos", default="")
	project_photo2 		= models.ImageField(upload_to="uploads/profile/project_photos", default="")
	project_photo3 		= models.ImageField(upload_to="uploads/profile/project_photos", default="")
	project_photo4 		= models.ImageField(upload_to="uploads/profile/project_photos", default="")
	description 		= RichTextUploadingField(blank=True,null=True)


	def __str__(self):
		return self.title

