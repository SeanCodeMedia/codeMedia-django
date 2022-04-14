from django.shortcuts import render

# Create your views here.


def show_videos(request):

	return render(request, "videos/videos.html") 