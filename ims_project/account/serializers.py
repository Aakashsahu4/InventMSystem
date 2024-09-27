"""External Imports"""
from rest_framework import serializers

"""Internal Imports"""
from account import models as account_models


class UserDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = account_models.UserData
        fields = ['phone','password']