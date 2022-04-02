from django.shortcuts import render
from blog.models import BlogPost

from portfolio.models import Project
from .models import  Home

# Create your views here.

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
	  "project"			:Project.objects.all(),
	  "Blog"   			:BlogPost.objects.all().order_by('-published')[:1], #todo fix this to add more to page
	  "range"  			:range(5),
	  "Home" 		    :Home.objects.all(),
	  "main_description":Home.objects.all().filter(id=1)[0],
	}


	return render(request, "home/index.html", context) 