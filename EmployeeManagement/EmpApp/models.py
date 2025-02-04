from django.db import models

# Create your models here.

class EmployeeDB(models.Model):
    Emp_ID = models.IntegerField(null=True,blank=True)
    Name = models.CharField(max_length=100,null=True,blank=True)
    Age = models.IntegerField(null=True,blank=True)
    Company = models.CharField(max_length=150,null=True,blank=True)
    Salary = models.IntegerField(null=True,blank=True)
    Location = models.CharField(max_length=100,null=True,blank=True)

