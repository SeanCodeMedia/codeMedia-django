from django.shortcuts 				 import render
from blog.models 					 import BlogPost
import os
from SeanCodeMedia                   import  settings
from portfolio.models 				 import Project
from .models 						 import  Home
from django.http 					 import HttpResponse
from django.http 					 import Http404
# Create your views here.


def download_resume(request):
	_file_name = Home.objects.all()[0].file_name
	path = "uploads/home/resume/"+_file_name
	file_path = os.path.join(settings.MEDIA_URL, path)
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