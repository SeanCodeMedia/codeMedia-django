# Generated by Django 3.1.2 on 2022-03-29 12:04

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20220329_0742'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='Degree_3_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]