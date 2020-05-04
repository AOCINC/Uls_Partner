from django.db import models
from django.core.validators import RegexValidator
from datetime import date
from datetime import datetime




List_Duration = ( 
    ("1", "1"), 
    ("2", "2"), 
    ("3", "3"), 
    ("4", "4"), 
    ("5", "5"), 
    ("6", "6"), 
    ("7", "7"), 
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
    ("11", "11"),
    ("12", "12"),
) 

In_Total_Duration= (
    ("WEEKS","WEEKS"),
    ("MONTHS", "MONTHS"),
    ("YEAR", "YEAR"),
   
)

class Projects(models.Model):
    ''' 
    this projects models used to take the inputs from the partner 

    '''
    Title              = models.CharField(max_length=49)
    Description        = models.TextField()
    Location           = models.CharField(max_length = 49)
    Linkedin_Profile   = models.CharField(max_length = 79,default = '')
    Posted_On          = models.DateTimeField(default=datetime.now)
    Duration           = models.CharField(max_length = 20, choices = In_Total_Duration)
    In                 = models.CharField(max_length = 29, choices = List_Duration)


