from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'job_type', 'salary', 'is_active')
    list_filter = ('job_type', 'location')
    search_fields = ('title',)