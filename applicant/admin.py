from django.contrib import admin
from .models import Applicant


class ApplicantAdmin(admin.ModelAdmin):
    # List of fields to display in the change list
    list_display = ['name', 'email', 'applied_on', 'created_on', 'modified_on']
    
admin.site.register(Applicant, ApplicantAdmin)