# Generated by Django 2.0.4 on 2019-02-04 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0023_auto_20190204_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='git',
            field=models.URLField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='languag',
            field=models.TextField(null=True),
        ),
    ]
