from django.contrib import admin
from . import models

@admin.register(models.Sheet)
class SheetAdmin(admin.ModelAdmin):
    list_display = (
        'defect',
        'process',
        'period',
        'created',   
    )
    search_fields = (
        'defect',
    )

    def __str__(self):
        return self.Sheet

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'author',
        'created',
        'updated',
    )

    def __str__(self):
        return self.text

@admin.register(models.AjaxImage)
class AjaxImageAdmin(admin.ModelAdmin):
    list_display = (
        'image_coord',  
    )
