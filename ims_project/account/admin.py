"""External Imports"""
from django.contrib import admin

"""Internal Imports"""
from account import models as account_models

@admin.register(account_models.UserData)
class UserDataAdmin(admin.ModelAdmin):
    list_display = ['phone','created','modified']