# Generated by Django 3.1.2 on 2022-04-10 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_home_filename'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home',
            old_name='fileName',
            new_name='file_name',
        ),
    ]