"""External Imports"""
from django.urls import path, include

"""Internal Imports"""
from item import views as item_views

urlpatterns = [
    path('create-item/',item_views.CreateItemAPI.as_view()),
    path('item/<str:id>/',item_views.GetItemsAPI.as_view()),
    path('items/',item_views.GetAllItemsAPI.as_view()),
    path('update-item/<str:id>/',item_views.UpdateItemAPI.as_view()),
    path('delete-item/<str:id>/',item_views.DeleteItemAPI.as_view()),
]