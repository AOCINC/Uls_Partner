from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.validators import RegexValidator
from TutorsInfo.Education_List import Education_list  # this is tuple for education list used in Education in Tutors table

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






class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', default='default.jpg')
    Education  = models.CharField(max_length = 30,default = 'Degree', choices = Education_list)
    Certified_In  = models.CharField(max_length = 39,default = '',blank = True,help_text = "You Can Add Your Certifications Here..")
    Country = models.CharField(max_length = 59,default = '',blank = True)
    State = models.CharField(max_length = 59,default = '',blank = True)
    Languages_Spoken  = models.CharField(max_length = 39,default = 'English',blank = True)
    Subjects =  models.CharField(max_length = 79, help_text = "Ex:various Subjects Your Teach..." ,default='')
    Expertise_Subject = models.CharField(max_length = 79, help_text = "Ex:JavaScript,Python,English,Algorithms,etc.," , default='')
    Year_Of_Experience = models.CharField(max_length = 20, choices = yr_exp,default = '4')  
    Teaching_Experience = models.TextField(default = 'GOOD') 
    Youtube_Subject = models.CharField(max_length = 79,default = '', blank = True,help_text = "Ex:JavaScript,Python,English,Algorithms,etc.,")
    Youtube_Url = models.CharField(max_length = 159,default = '', blank = True,help_text = "Your Youtube Channel URL")
    Company = models.CharField(max_length=89)
    Adhar_Number = models.CharField(max_length=12,validators=[RegexValidator(r'^\d{1,12}$')], default='Adhar Number')
    Phone_Number = models.CharField(max_length=12,validators = [RegexValidator(r'^\d{1,12}$')], default = 'Mobile Number')
    GST_Number   = models.CharField(max_length = 15, blank=True)
    Pan_Number   = models.CharField(max_length=10, default ='PAN Number', blank = True)
    CIN_Number   = models.CharField(max_length = 21, blank = True)
    Company_Postal_Address = models.CharField(max_length=89, default="Complete Address")
    FullName     = models.CharField(max_length = 79,default = '')
    Bank_Account_Number = models.CharField(max_length=12,default="Bank Account Number")
    IFSC = models.CharField(max_length=11,default="IFSC CODE")
    Branch =models.CharField(max_length=29,default="Branch Name")
   

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args, **kwags):
        super(Profile, self).save()

        img = Image.open(self.image.path)
        if img.height > 300 and img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



