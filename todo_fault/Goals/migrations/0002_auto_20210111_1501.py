# Generated by Django 3.1.5 on 2021-01-11 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Goals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='parent_list',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.IntegerField(default=0),
        ),
    ]