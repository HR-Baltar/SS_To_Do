# Generated by Django 3.1.5 on 2021-01-09 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Goals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]