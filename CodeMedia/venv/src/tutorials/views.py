from django.shortcuts import render
from .models import  Category
from .models import  BlogPost
from SeanCodeMedia.settings import MEDIA_ROOT, MEDIA_URL
# Create your views here.

def show_tutorials(request):

	context={

	"Category": Category.objects.all(),
	'media_root': MEDIA_ROOT.replace("/media",""), 
	'media_url': MEDIA_URL

	}
	return render(request, "tutorials/tutorials.html", context) 


def show_articles(request,category_id_):

	#print(category_id)

	context = {

	"BlogPost": BlogPost.objects.all().filter(category_id=int(category_id_)),

	}

	return render(request, "tutorials/articles.html", context) 



def show_blog_post(request,category_id_,blog_post_id):

	posts 		= BlogPost.objects.all().filter(category_id=int(category_id_))

	context = {

	"title"          		: 	 posts[int(blog_post_id)-1].title,
	"author"         		:	 posts[int(blog_post_id)-1].author,
	"author_photo"     		:     posts[int(blog_post_id)-1].author_photo,
	"published"      		:     posts[int(blog_post_id)-1].published,
	"overview"   		    :     posts[int(blog_post_id)-1].overview,
	"main_coverImage"		:     posts[int(blog_post_id)-1].main_coverImage,
	"body"           		:     posts[int(blog_post_id)-1].body,

	}

	return render(request, "tutorials/blog_post.html", context) 







