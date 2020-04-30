from django.contrib import admin
from .models import Projects

class ProjectAdmin(admin.ModelAdmin):
    list_display = [
                    'Title',
                    'Description',
                    'Location',
                    'Posted_On',
                    'In',
                    'Duration',
                    
    ]

admin.site.register(Projects,ProjectAdmin)
