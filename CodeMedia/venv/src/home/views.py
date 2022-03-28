from django.shortcuts import render
from tutorials.models import BlogPost
from portfolio.models import Project
from .models import  Home

# Create your views here.

def index(request):
	# optimize this uisng a array
	try:
		mostRecent1 = BlogPost.objects.all().reverse()[0]; 
	except Exception as e:
		mostRecent1 = ""

	try:
		mostRecent2 = BlogPost.objects.all().reverse()[1]; 
	except Exception as e:
		mostRecent2 = ""

	try:
		mostRecent3 = BlogPost.objects.all().reverse()[2]; 
	except Exception as e:
		mostRecent3 = ""

	try:
		mostRecent4 = BlogPost.objects.all().reverse()[3]; 
	except Exception as e:
		mostRecent4 = ""

	try:
		mostRecent5 = BlogPost.objects.all().reverse()[4]; 
	except Exception as e:
		mostRecent5 = ""

	context = {
	  "project":Project.objects.all(),
	  "post1":mostRecent1,
	  "post2":mostRecent2,
	  "post3":mostRecent3,
	  "post4":mostRecent4,
	  "post5":mostRecent5,
	  "range":range(5),
	  "Home":Home.objects.all(),
	  "main_description":Home.objects.all().filter(id=1)[0],
	}


	return render(request, "home/index.html", context) 