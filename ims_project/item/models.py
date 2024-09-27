""""External Imports"""
from django.db import models
import uuid


class ItemsData(models.Model):
    """Model to store Item Datas"""

    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False) 
    name = models.CharField(max_length=50,unique=True)
    description = models.TextField(null=True,blank=True)
    
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)