from django.db import models

# Create your models here.

class Library(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=100,null=True,blank=True)
    Age = models.IntegerField(null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Email_Id = models.EmailField(max_length=100,null=True,blank=True)
    Place = models.CharField(max_length=100,null=True,blank=True)
    Profile_Image = models.CharField(max_length=100,null=True,blank=True)
