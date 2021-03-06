# Generated by Django 3.1.2 on 2020-11-08 22:03

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20201026_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_photo1',
            field=models.ImageField(default='', upload_to='uploads/profile/project_photos'),
        ),
        migrations.AddField(
            model_name='project',
            name='project_photo2',
            field=models.ImageField(default='', upload_to='uploads/profile/project_photos'),
        ),
        migrations.AddField(
            model_name='project',
            name='project_photo3',
            field=models.ImageField(default='', upload_to='uploads/profile/project_photos'),
        ),
        migrations.AddField(
            model_name='project',
            name='short_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='githubLlink',
            field=models.URLField(default='https://github.com/SeanCodeMedia'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
