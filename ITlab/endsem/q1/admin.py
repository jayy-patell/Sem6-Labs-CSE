from django.contrib import admin
from . import models

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name','joining_date']
admin.site.register(models.Employee, EmployeeAdmin)

# Register your models here.
