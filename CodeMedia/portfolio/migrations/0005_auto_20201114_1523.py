# Generated by Django 3.1.2 on 2020-11-14 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20201108_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='linkedinLlink',
            field=models.URLField(default='https://www.linkedin.com/in/seanpeart/'),
        ),
        migrations.AddField(
            model_name='project',
            name='youtubeLink',
            field=models.URLField(default='https://www.youtube.com/channel/UC8qa9USnmzi-ewkXTMiZ9LA?view_as=subscriber'),
        ),
    ]