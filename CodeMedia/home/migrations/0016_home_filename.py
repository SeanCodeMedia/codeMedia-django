# Generated by Django 3.1.2 on 2022-04-10 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20220410_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='fileName',
            field=models.CharField(default='resume.pdf', max_length=100),
        ),
    ]