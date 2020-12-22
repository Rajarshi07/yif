from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
Gender = (('M','Male'),('F','Female'),('O','Others'))
class Member(models.Model):
    Name = models.CharField(max_length=100,null=False,blank=False)
    Email = models.EmailField(null=False,blank=False,unique=True)
    Mobile = PhoneNumberField(null=False,blank=False)
    Gender = models.CharField(choices=Gender,max_length=6,blank=True)
    