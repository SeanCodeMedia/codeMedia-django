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
	about_cv  			= RichTextUploadingField(blank=True,null=True)
	Education_1 		= models.CharField(max_length=100, default="Bard High School")
	Education_2 		= models.CharField(max_length=100, default="Bard Early College")
	Education_3			= models.CharField(max_length=100, default="Montclair State University")
	Degree_1 			= models.CharField(max_length=100, default="High School Diploma")
	Degree_2 			= models.CharField(max_length=100, default="Associate Degree In Liberal Arts")
	Degree_3 			= models.CharField(max_length=100, default="Bachelor Of Science In Computer Science")
	Year_1 				= models.CharField(max_length=100, default="2012-2013")
	Year_2 				= models.CharField(max_length=100, default="2013-2015")
	Year_3 				= models.CharField(max_length=100, default="2015-2018")
	Experience_1 		= models.CharField(max_length=100, default="Third Prism Studios")
	Experience_year_1 	= models.CharField(max_length=100, default="2017-2018")
	Experience_2		= models.CharField(max_length=100, default="Igloo Vision USA")
	Experience_year_2 	= models.CharField(max_length=100, default="2018-Present")
	Degree_1_description= RichTextUploadingField(blank=True,null=True)
	Degree_2_description= RichTextUploadingField(blank=True,null=True)
	Degree_3_description= RichTextUploadingField(blank=True,null=True)
	Experience_1_description= RichTextUploadingField(blank=True,null=True)
	Experience_2_description= RichTextUploadingField(blank=True,null=True)
	role1 				= models.CharField(max_length=100, default="Web Developer")
	role2 				= models.CharField(max_length=100, default="Application Engineer")
	# icon2		 		= models.ImageField(upload_to="uploads/profile/project_photos", default="")
	# icon3		 		= models.ImageField(upload_to="uploads/profile/project_photos", default="")

	# about_me_photo		= models.ImageField(upload_to="uploads/profile/project_photos", default="")
	# course_paid_text	= RichTextUploadingField(blank=True,null=True)
	# course_paid_photo	= models.ImageField(upload_to="uploads/profile/project_photos", default="")
	# donate_text			= RichTextUploadingField(blank=True,null=True)
	# donate_photo	    = models.ImageField(upload_to="uploads/profile/project_photos", default="")



	def __str__(self):
		return self.title
