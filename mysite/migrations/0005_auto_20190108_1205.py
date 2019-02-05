# Generated by Django 2.0.4 on 2019-01-08 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20190108_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('Image', models.ImageField(blank=True, null=True, upload_to='chapter/%Y/%m/%D/')),
                ('by', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.DeleteModel(
            name='Imagee',
        ),
    ]