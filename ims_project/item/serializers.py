"""External Imports"""
from rest_framework import serializers

"""Internal Imports"""
from item import models as item_models


class ItemDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = item_models.ItemsData
        fields = ['id','name','description']