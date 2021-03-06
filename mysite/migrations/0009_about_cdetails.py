# Generated by Django 2.0.4 on 2019-01-08 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_auto_20190108_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField()),
                ('document', models.FileField(blank=True, null=True, upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Cdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
            ],
        ),
    ]
