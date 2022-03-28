from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
# Create your views here.
def show_portfolio(request):

	context = {
	  "project":Project.objects.all()
	}

	return render(request, "portfolio/portfolio.html", context)



def show_project(request, project_id):

	context = {
	    "project":Project.objects.all().filter(id=int(project_id)),
	}

	print(Project.objects.all().filter(id=int(project_id)))

	return render(request, "portfolio/project.html", context)
