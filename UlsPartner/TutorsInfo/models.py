from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .Education_List import Education_list  # this is tuple for education list used in Education in Tutors table

yr_exp = (
          ('4','4'),
          ('5','5'),
          ('6','6'),
          ('7','7'),
          ('8','8'),
          ('9','9'),
          ('10','10'),
          ('11','11'),
          ('12','12'),
          ('13','13'),
          ('14','14'),
          )





class Tutors(models.Model):
    user =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null = True)
    Education  = models.CharField(max_length = 30,default = 'Degree', choices = Education_list)
    Certified_In  = models.CharField(max_length = 39,default = '',blank = True,help_text = "You Can Add Your Certifications Here..")
    Email = models.EmailField(max_length = 59, blank = False)
    Phone_Number = models.CharField(max_length=15,validators = [RegexValidator(r'^\d{1,15}$')])
    Country = models.CharField(max_length = 59)
    State = models.CharField(max_length = 59)
    Languages_Spoken  = models.CharField(max_length = 39,default = 'English',blank = True)
    Subjects =  models.CharField(max_length = 79, help_text = "Ex:various Subjects Your Teach..." ,default='')
    Expertise_Subject = models.CharField(max_length = 79, help_text = "Ex:JavaScript,Python,English,Algorithms,etc.," , default='')
    Year_Of_Experience = models.CharField(max_length = 20, choices = yr_exp,default = '4')  
    Teaching_Experience = models.TextField(default = 'GOOD') 

    @staticmethod
    def get_Tutor_Data_by_ids(name):
        return Tutors.objects.filter(user = name)





class Youtubers(models.Model):
    Email = models.EmailField(max_length = 59, blank = False)
    Phone_Number = models.CharField(max_length=15,validators = [RegexValidator(r'^\d{1,15}$')])
    Country = models.CharField(max_length = 59)
    State = models.CharField(max_length = 59)
    Youtube_Subject = models.CharField(max_length = 79, help_text = "Ex:JavaScript,Python,English,Algorithms,etc.,")
    Youtube_Url = models.CharField(max_length = 159, help_text = "Your Youtube Channel URL")
    