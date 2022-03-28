from django.contrib import admin
from tutorials.models import BlogPost
from portfolio.models import Project
from tutorials.models import Category
from home.models import Home
# Register your models here.

admin.site.register(BlogPost)
admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Home)