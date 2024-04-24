from django.contrib import admin
from . import models

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','visits','likes']
admin.site.register(models.CategoryModel, CategoryAdmin)

class PageAdmin(admin.ModelAdmin):
    list_display=['category','title','views','url']
admin.site.register(models.PageModel, PageAdmin)

# Register your models here.
