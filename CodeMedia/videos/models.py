from django.db import models


from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Video(models.Model):

	title 				= models.CharField(max_length=100, default="Videos")
	about_channel	 	= RichTextUploadingField(blank=True,null=True)
	# icon2		 		= models.ImageField(upload_to="uploads/profile/project_photos", default="")
	# icon3		 		= models.ImageField(upload_to="uploads/profile/project_photos", default="")

	# about_me_photo		= models.ImageField(upload_to="uploads/profile/project_photos", default="")
	# course_paid_text	= RichTextUploadingField(blank=True,null=True)
	# course_paid_photo	= models.ImageField(upload_to="uploads/profile/project_photos", default="")
	# donate_text			= RichTextUploadingField(blank=True,null=True)
	# donate_photo	    = models.ImageField(upload_to="uploads/profile/project_photos", default="")



	def __str__(self):
		return self.title

