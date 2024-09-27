""""External Imports"""
from django.urls import path

"""Internal Imports"""
from account import views

urlpatterns = [
    path('sign-up/',views.UserSignUpAPI.as_view()),
    path('login/',views.UserLoginAPI.as_view()),
    
    # refresh Token API x
    # readme
    # redis -------------
    # logging
    # test cases x
]