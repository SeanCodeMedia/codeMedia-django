from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Home(models.Model):

	title 				= models.CharField(max_length=100, default="Home")
	facebook 			= models.CharField(max_length=500, default="https://www.facebook.com/")
	instagram 			= models.CharField(max_length=500, default="https://www.instagram.com/?hl=en")
	youtube 			= models.CharField(max_length=500, default="https://www.youtube.com/channel/UC8qa9USnmzi-ewkXTMiZ9LA")
	email 				= models.CharField(max_length=100, default="codemedia32@gmail.com")
	main_photo			= models.ImageField(upload_to="uploads/home/homephotos", default="")
	main_photo_2		= models.ImageField(upload_to="uploads/home/homephotos", default="")
	main_photo_3		= models.ImageField(upload_to="uploads/home/homephotos", default="")
	about_me			= RichTextUploadingField(blank=True,null=True)
	skill_description 	= RichTextUploadingField(blank=True,null=True)
	about_youtube	 	= RichTextUploadingField(blank=True,null=True)

	# icon2		 		= models.ImageField(upload_to="uploads/profile/project_photos", default="")
	# icon3		 		= models.ImageField(upload_to="uploads/profile/project_photos", default="")

	# about_me_photo		= models.ImageField(upload_to="uploads/profile/project_photos", default="")
	# course_paid_text	= RichTextUploadingField(blank=True,null=True)
	# course_paid_photo	= models.ImageField(upload_to="uploads/profile/project_photos", default="")
	# donate_text			= RichTextUploadingField(blank=True,null=True)
	# donate_photo	    = models.ImageField(upload_to="uploads/profile/project_photos", default="")



	def __str__(self):
		return self.title
