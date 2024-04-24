from django.contrib import admin
from . import models

class BookAdmin(admin.ModelAdmin):
    list_display = ['title','pubdate','authors','publication']
admin.site.register(models.BookModel, BookAdmin)

# Register your models here.
