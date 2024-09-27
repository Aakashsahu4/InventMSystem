"""External Imports"""
from django.contrib import admin

"""Internal Imports"""
from item import models as item_models

@admin.register(item_models.ItemsData)
class ItemsDataAdmin(admin.ModelAdmin):
    list_display = ['id','name','description','created','modified']