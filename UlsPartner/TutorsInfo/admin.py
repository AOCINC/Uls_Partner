from django.contrib import admin
from .models import Tutors


class TutorsAdmin(admin.ModelAdmin):
    list_display = [
                    'Email',
                    'Phone_Number',
                    'Country',
                    'State',
                    'Youtube_Subject',
                    'Youtube_Url',

                        
                    ]


admin.site.register(Tutors,TutorsAdmin)