from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime,date
from datetime import datetime



# Create your models here.
class Student (models.Model):
    userName= models.CharField(max_length=60)
    first_name= models.CharField(max_length=60)
    last_name= models.CharField(max_length=60)
    email= models.EmailField()
    password=models.CharField(max_length=60,default='')
    phone=models.IntegerField()
    def __str__(self):
        return self.first_name


class Faculty (models.Model):
    userName= models.CharField(max_length=60)
    first_name= models.CharField(max_length=60)
    last_name= models.CharField(max_length=60)
    email= models.EmailField()
    password=models.CharField(max_length=60,default='')

class ProposedTopic(models.Model):
    topicname=models.CharField(max_length=50,blank=False)
    member1=models.CharField(max_length=30,blank=False)
    member2=models.CharField(max_length=30,blank=False)
    member3=models.CharField(max_length=30,blank=True)
    paper1=models.CharField(max_length=30,blank=False)
    paper2=models.CharField(max_length=30,blank=False)
    paper3=models.CharField(max_length=30,blank=False)
    paper4=models.CharField(max_length=30,blank=False)
    paper5=models.CharField(max_length=30,blank=False)

    def __str__(self):
        return self.topicname +' - '+ self.member1 +' - '+ self.member2 +' - '+ self.member3

class MeetingTable(models.Model):
    topicname=models.CharField(max_length=50,blank=False)
    date=models.DateField(auto_now_add=False,auto_now=False)
    time=models.TimeField()
    room=models.CharField(max_length=30,blank=False)

    def __str__(self):
        return str (self.topicname +' - '+self.date.strftime(" %d %b %Y") + ' - ' + self.time.strftime("%I %M %p")+ ' - ' +self.room)

class GradeTable(models.Model):
    topicname=models.CharField(max_length=50,blank=False)
    credit=models.CharField(max_length=30,blank=False)
    grade=models.CharField(max_length=30,blank=False)
    gpa=models.CharField(max_length=30,blank=False)

    def __str__(self):
        return str (self.topicname +' - '+self.credit + ' - ' + self.grade+ ' - ' +self.gpa)

class Ad_panel (models.Model):
    userName= models.CharField(max_length=60)
    first_name= models.CharField(max_length=60,default='')
    last_name= models.CharField(max_length=60,default='')
    email= models.EmailField()
    password=models.CharField(max_length=60,default='')