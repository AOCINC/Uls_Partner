from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.validators import RegexValidator



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', default='default.jpg')
    Company = models.CharField(max_length=89)
    Adhar_Number = models.CharField(max_length=12,validators=[RegexValidator(r'^\d{1,12}$')], default='Adhar Number')
    Phone_Number = models.CharField(max_length=12,validators = [RegexValidator(r'^\d{1,12}$')], default = 'Mobile Number')
    GST_Number   = models.CharField(max_length = 15, blank=True)
    Pan_Number   = models.CharField(max_length=10, default ='PAN Number', blank = True)
    CIN_Number   = models.CharField(max_length = 21, blank = True)
    Company_Postal_Address = models.CharField(max_length=89, default="Complete Address")
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



