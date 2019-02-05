from django.db import models
from django.utils import timezone
import datetime


# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name


class Contact(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=196)
    message = models.TextField()



    def __str__(self):
        return self.email



class work(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(blank = True, null = True)
    by = models.CharField(max_length=50)
    pub_date = models.DateTimeField( 'date published' )

    def __str__( self ):
        return self.title

    def __unicode__(self):
        return self.title


    def was_published_recently( self ):
        now = timezone.now()
        return now - datetime.timedelta( days = 1 ) <= self.pub_date <= now

class About(models.Model):
    detail = models.TextField()
    document = models.FileField(blank = True, null = True )
    image = models.ImageField(blank = True, null = True )
    buniversity = models.CharField(max_length=100,null = True )
    blocation = models.CharField(max_length=100,null = True )
    bgpa = models.CharField(max_length=5,null = True )
    muniversity = models.CharField(max_length=100,null = True )
    mlocation = models.CharField(max_length=100,null = True )
    mgpa = models.CharField(max_length=5,null = True )
    bmajor = models.CharField(max_length=100,null = True )
    mmajor = models.CharField(max_length=100,null = True )
    slide = models.ImageField(blank = True, null = True )


    def __str__( self ):
        return self.detail



class Cdetail(models.Model):
    phone = models.CharField( max_length = 30 )
    email = models.EmailField()
    address = models.TextField()
    pub_date = models.DateTimeField( 'date published' )

    def __str__( self ):
        return self.phone

    def was_published_recently( self ):
        now = timezone.now()
        return now - datetime.timedelta( days = 1 ) <= self.pub_date <= now


class blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(blank = True, null = True )#upload_to="chapter/%Y/%m/%D/"
    by = models.CharField(max_length=50)
    link = models.URLField(max_length=150)
    body = models.CharField(max_length= 300, null=True)
    github = models.URLField(max_length=150, blank=True, null=True)
    language = models.TextField(null=True)
    pub_date = models.DateTimeField( 'date published' )

    def __str__( self ):
        return self.title

    def was_published_recently( self ):
        now = timezone.now()
        return now - datetime.timedelta( days = 1 ) <= self.pub_date <= now




