from django.contrib import admin
from tutorials.models import BlogPost
from tutorials.models import Category

# Register your models here.

admin.site.register(BlogPost)
admin.site.register(Category)
