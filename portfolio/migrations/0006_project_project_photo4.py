# Generated by Django 3.1.2 on 2022-03-27 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20201114_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_photo4',
            field=models.ImageField(default='', upload_to='uploads/profile/project_photos'),
        ),
    ]
