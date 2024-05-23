from django.contrib import admin
from .models import Job

admin.site.site_header = 'EternalJobs'      # default: "Django Administration"
admin.site.index_title = 'Site administration'   # default: "Site administration"
admin.site.site_title = 'EternalJobs Login'  # default: "Django site admin"

class JobAdmin(admin.ModelAdmin):
    # List of fields to display in the change list
    list_display = ['title', 'company_name', 'created_on', 'modified_on']
    
    # List of fields to hide in the change form
    exclude = ['slug']

admin.site.register(Job, JobAdmin)