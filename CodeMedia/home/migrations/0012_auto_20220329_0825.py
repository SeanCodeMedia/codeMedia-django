# Generated by Django 3.1.2 on 2022-03-29 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_home_degree_3_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='role1',
            field=models.CharField(default='Web Developer', max_length=100),
        ),
        migrations.AddField(
            model_name='home',
            name='role2',
            field=models.CharField(default='Application Engineer', max_length=100),
        ),
    ]