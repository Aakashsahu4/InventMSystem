"""External Imports"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

"""Internal Imports"""
from account import serializers as account_serializers
from account import models as account_models
from master import keys, messages



class UserSignUpAPI(APIView):
    """API for user Sign up"""
    def post(self,request):
        request_data = request.data.copy()
        phone = request_data['phone']

        queryset = account_models.UserData.objects.filter(phone=phone)
        if queryset:
            return Response({keys.SUCCESS:False,keys.MESSAGE:messages.USER_EXISTS},status=status.HTTP_400_BAD_REQUEST)

        serializer = account_serializers.UserDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({keys.SUCCESS:True,keys.DATA:serializer.data},status=status.HTTP_201_CREATED)
        return Response({keys.SUCCESS:False,keys.MESSAGE:serializer.errors},status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPI(APIView):
    """User Login API"""

    def post(self,request):
        phone = request.data.get('phone')
        password = request.data.get('password')
        queryset = account_models.UserData.objects.filter(phone=phone,password=password)
        if queryset:
            user_instance = account_models.UserData.objects.get(phone=phone,password=password)
            refresh = RefreshToken.for_user(user_instance)
            return Response({
                keys.SUCCESS:True,keys.MESSAGE:messages.LOGIN_SUCCESSFULL,'refresh': str(refresh),'access': str(refresh.access_token),},status=status.HTTP_200_OK)
        return Response({keys.SUCCESS:False,keys.MESSAGE:messages.ACCOUNT_DOES_NOT_EXISTS},status=status.HTTP_404_NOT_FOUND)

