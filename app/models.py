from django.db import models
import django.utils.timezone
from django.contrib.auth.models import User
# from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
Gender = (('Male','Male'),('Female','Female'),('Others','Others'))
Divisions = (('National','National'),('State','States'),('Society','Society'),('Outreach','Outreach'),('Initiative','Initiative'))
Education = (('School','School'),('College','College'),('Graduate','Graduate'),('PostGraduate','Post Graduate'))
Department = (('Marketing','Marketing'),('IT','IT'),('Management','Management'),('PR','Public Relations'),('Finance','Finance'),('HR','Human Resource'))
TS = (('11-1','11am to 1pm'),('2-4','2pm to 4pm'),('5-7','5pm to 7pm'))

class Position(models.Model):
    Name = models.CharField(max_length = 50)
    Department = models.CharField(choices=Department,max_length=10,blank=False)
    def __str__(self):
        return self.Name+', '+self.Department
class Outreach(models.Model):
    Name = models.CharField(max_length = 50)
    Url = models.CharField(max_length=120,null=True,blank=True)
    def __str__(self):
        return self.Name
class State(models.Model):
    Name = models.CharField(max_length = 50)
    Url = models.CharField(max_length=120,null=True,blank=True)
    def __str__(self):
        return self.Name
class Society(models.Model):
    Name = models.CharField(max_length = 50)
    Url = models.CharField(max_length=120,null=True,blank=True)
    def __str__(self):
        return self.Name
class Initiative(models.Model):
    Name = models.CharField(max_length = 50)
    Url = models.CharField(max_length=120,null=True,blank=True)
    def __str__(self):
        return self.Name

class Member(models.Model):
    Name = models.CharField(max_length=100,null=False,blank=False)
    Email = models.EmailField(null=False,blank=False,unique=True)
    Mobile = models.CharField(max_length=12,null=False,blank=False)
    Gender = models.CharField(choices=Gender,max_length=6,blank=True)
    Division = models.CharField(choices=Divisions,max_length=12,blank=False)
    State = models.ForeignKey(State,on_delete=models.CASCADE,null=True,blank=True)
    Outreach = models.ForeignKey(Outreach,on_delete=models.CASCADE,null=True,blank=True)
    Society = models.ForeignKey(Society,on_delete=models.CASCADE,null=True,blank=True)
    Initiative =models.ForeignKey(Initiative,on_delete=models.SET_NULL,null=True,blank=True)
    City = models.CharField(max_length=20,null=False,blank=False)
    Education = models.CharField(choices=Education,max_length=15,blank=False)
    InstituteName = models.CharField(max_length=100,null=False,blank=False)
    Std = models.CharField(max_length=3,null=False,blank=False)
    Department = models.CharField(choices=Department,max_length=10,blank=False)
    Position = models.ForeignKey(Position,on_delete=models.SET_NULL,null=True,blank=True)
    WhyHire = models.CharField(max_length=255,null=False,blank=False)
    WhyJoin = models.CharField(max_length=255,null=False,blank=False)
    Timeslot = models.CharField(choices=TS,max_length=5,blank=False)
    Resume = models.FileField(upload_to='resumes',default="")
    IsActive = models.BooleanField(default=False)
    def __str__(self):
        return self.Name

class Contact(models.Model):
    name = models.CharField(max_length = 100,null=False,blank=False)
    email = models.EmailField(max_length = 100)
    message = models.CharField(max_length= 500)
    date = models.DateField(blank = True, default = django.utils.timezone.now)
    def __str__(self):
        return self.name+self.message

class Circular(models.Model):
    Name = models.CharField(max_length = 100,null=False,blank=False)
    url = models.CharField(max_length = 255,null=False,blank=False)
    TimeAdded = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Name

class NEW(models.Model):
    Title = models.CharField(max_length = 100,null=False,blank=False,default="Title")
    Subtitle = models.CharField(max_length = 50,null=True,blank=True,default="subtitle")
    Content = models.TextField(null=True,blank=True,default="content")
    def __str__(self):
        return self.Title


class File(models.Model):
    user = models.OneToOneField(User,related_name='owner',on_delete=models.CASCADE)
    Name = models.CharField(max_length = 100,null=True,blank=True)
    File = models.FileField(upload_to='files',default="")
    def __str__(self):
        return self.Name

