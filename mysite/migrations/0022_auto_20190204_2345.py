# Generated by Django 2.0.4 on 2019-02-04 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0021_auto_20190204_2343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='language',
            new_name='languag',
        ),
    ]
