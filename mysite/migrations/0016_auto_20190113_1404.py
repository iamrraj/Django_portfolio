# Generated by Django 2.0.4 on 2019-01-13 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0015_auto_20190108_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='body',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='link',
            field=models.URLField(max_length=150),
        ),
    ]