# Generated by Django 2.0.4 on 2019-01-08 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0013_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
