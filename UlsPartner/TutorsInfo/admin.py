from django.contrib import admin
from .models import Tutors, Youtubers


class TutorsAdmin(admin.ModelAdmin):
    list_display = [
                    'Email',
                    'Phone_Number',
                    'Country',
                    'State',
                    'Subjects',
                    'Expertise_Subject',

                        
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