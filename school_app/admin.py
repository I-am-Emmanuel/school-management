from django.contrib import admin
from . models import *

# Register your models here.

@admin.register(ParentOrGuardianModel)
class ParentOrGuardianAdmin(admin.ModelAdmin):
    list_display = ['profile_pics',]
