from django.shortcuts 				 import render
from blog.models 					 import BlogPost
import os
from SeanCodeMedia                   import  settings
from portfolio.models 				 import Project
from .models 						 import  Home
from django.http 					 import HttpResponse
from django.http 					 import Http404
# Create your views here.
import boto3
import botocore

session = boto3.session.Session()
client = session.client(
    's3',
    region_name='nyc3',
    endpoint_url=settings.AWS_S3_ENDPOINT_URL,
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
)

def download_resume(request):
	#_file_name = Home.objects.all()[0].file_name
	#path = "uploads/home/resume/"+_file_name
	print("RUNNNING")
	path = "Resume/Sean Peart Resume.pdf"
	# try:
	# 	client.download_file(Bucket=settings.AWS_STORAGE_BUCKET_NAME,
	# 						 Key='Resume.pdf',
	# 						 Filename='/media/uploads/home/resume/Resume.pdf',)


	# except botocore.exceptions.ClientError as e:
	# 	if e.response['Error']['Code'] == "404":
	# 		print("The object does not exist.")
	# 		Http404("sorry not found")
	# 	else:
	# 		Http404("sorry not found")

	file_path = os.path.join(settings.STATIC_ROOT, path)
	# file_path = "https://seancodemediadjango.sfo3.digitaloceanspaces.com/media/uploads/home/resume/Resume.pdf"
	print(file_path)
	if os.path.exists(file_path):
		with open(file_path, 'rb') as fh:
		    response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
		    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
		    return response
	raise Http404("sorry not found")

def index(request):
	# optimize this uisng a array
	# try:
	# 	mostRecent1 = BlogPost.objects.all().reverse()[0]; 
	# except Exception as e:
	# 	mostRecent1 = ""

	# try:
	# 	mostRecent2 = BlogPost.objects.all().reverse()[1]; 
	# except Exception as e:
	# 	mostRecent2 = ""

	# try:
	# 	mostRecent3 = BlogPost.objects.all().reverse()[2]; 
	# except Exception as e:
	# 	mostRecent3 = ""

	# try:
	# 	mostRecent4 = BlogPost.objects.all().reverse()[3]; 
	# except Exception as e:
	# 	mostRecent4 = ""

	# try:
	# 	mostRecent5 = BlogPost.objects.all().reverse()[4]; 
	# except Exception as e:
	# 	mostRecent5 = ""
     
    
	context = {
	  "project"			:Project.objects.all()[:6],
	  "Blog"   			:BlogPost.objects.all().filter(category=int(Home.objects.all()[0].home_page_category)).order_by('-published')[:6], #todo fix this to add more to page
	  "range"  			:range(5),
	  "Home" 		    :Home.objects.all(),
	  "main_description":Home.objects.all().filter(id=1)[0],
	}


	return render(request, "home/index.html", context) 