"""SeanCodeMedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib    import admin
from django.urls       import path, include
from home.views        import index
from tutorials.views   import show_tutorials
from tutorials.views   import show_articles
from tutorials.views   import  show_blog_post
from portfolio.views   import show_portfolio
from portfolio.views   import show_project
from ckeditor_uploader import urls
from django.conf       import  settings
from django.conf.urls.static  import  static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from SeanCodeMedia import  settings

admin.site.site_header = "Code Meida Admin"
admin.site.site_title = "Code Media Admin Portal"
admin.site.index_title = "Welcome to Sean Code Media Portal"


urlpatterns = [
	path('', index),
	path('tutorials/',show_tutorials),
    path("tutorials/articles/<category_id_>/",show_articles),
    path("tutorials/articles/<category_id_>/blogpost/<blog_post_id>/",show_blog_post),
	path('portfolio/', show_portfolio),
    path('portfolio/project/<project_id>/', show_project),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),

] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

