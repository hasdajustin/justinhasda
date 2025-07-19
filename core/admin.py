from django.contrib import admin
from .models import Project
from .models import Contact
from .models import HireRequest

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    search_fields = ['name', 'email', 'subject']

@admin.register(HireRequest)
class HireRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'project_type', 'created_at']
    search_fields = ['name', 'email', 'project_type']