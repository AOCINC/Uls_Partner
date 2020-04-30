from django.db import models
from django.core.validators import RegexValidator



class Tutors(models.Model):
    Email = models.EmailField(max_length = 59, blank = False)
    Phone_Number = models.CharField(max_length=15,validators = [RegexValidator(r'^\d{1,15}$')])
    Country = models.CharField(max_length = 59)
    State = models.CharField(max_length = 59)
    Youtube_Subject = models.CharField(max_length = 79, help_text = "Ex:JavaScript,Python,English,Algorithms,etc.,")
    Youtube_Url = models.CharField(max_length = 159, help_text = "Your Youtube Channel URL")
