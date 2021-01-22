from django.contrib import admin
from .models import Tutors, Youtubers


class TutorsAdmin(admin.ModelAdmin):
    list_display = [
                    'user',
                    'Education',
                    'Certified_In',                    
                    'Email',
                    'Phone_Number',
                    'Country',
                    'State',
                    'Languages_Spoken',
                    'Subjects',
                    'Expertise_Subject',
                    'Year_Of_Experience',
                    'Teaching_Experience',
                        
                    ]


class YoutubersAdmin(admin.ModelAdmin):
    list_display = [
                    'Email',
                    'Phone_Number',
                    'Country',
                    'State',
                    'Youtube_Subject',
                    'Youtube_Url',
                        
    ]
admin.site.register(Youtubers,YoutubersAdmin)
admin.site.register(Tutors,TutorsAdmin)