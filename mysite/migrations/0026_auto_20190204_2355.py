# Generated by Django 2.0.4 on 2019-02-04 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0025_auto_20190204_2351'),
    ]

    operations = [
        migrations.DeleteModel(
            name='blog1',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='gihub',
            new_name='github',
        ),
    ]
