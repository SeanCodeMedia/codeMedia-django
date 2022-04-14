# Generated by Django 3.1.2 on 2022-03-29 20:34

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('overview', models.CharField(default='', max_length=100)),
                ('coverImage', models.ImageField(upload_to='uploads/categories')),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='Sean Peart', max_length=50)),
                ('author_photo', models.ImageField(default='', upload_to='uploads/author_photos')),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=100)),
                ('overview', models.TextField(max_length=100)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('body_2', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('main_coverImage', models.ImageField(default='', upload_to='uploads/blogImages')),
                ('category_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
            ],
        ),
    ]