"""External Imports"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.core.cache import cache

"""Internal Imports"""
from item import serializers as item_serializers
from item import models as item_models
from master import keys, messages



class CreateItemAPI(APIView):
    """API to Create Item"""

    permission_classes = [IsAuthenticated]

    def post(self,request):
        request_data = request.data.copy()
        request_data['name'] = request.data.get(keys.NAME)
        request_data['description'] = request.data.get(keys.DESCRIPTION)

        queryset = item_models.ItemsData.objects.filter(name=request_data['name'])
        if queryset:
            return Response({keys.SUCCESS:False,keys.MESSAGE:messages.ITEM_EXISTS},status=status.HTTP_400_BAD_REQUEST)

        serializer = item_serializers.ItemDataSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response({keys.SUCCESS:True,keys.DATA:serializer.data},status=status.HTTP_201_CREATED)
        return Response({keys.SUCCESS:False,keys.MESSAGE:serializer.errors},status=status.HTTP_400_BAD_REQUEST)


class GetItemsAPI(APIView):
    """API to retrieve Item Datas"""

    permission_classes = [IsAuthenticated]

    def get(self,request,id):
        item_queryset = cache.get('cached_queryset')

        if id:
            item_queryset = item_models.ItemsData.objects.filter(id=id)
            if item_queryset:
                item_instance = item_models.ItemsData.objects.get(id=id)
                serializer = item_serializers.ItemDataSerializer(item_instance)
                cache.set('cached_queryset', serializer.data, timeout=60*60)
                return Response({keys.SUCCESS:True,keys.DATA:serializer.data},status=status.HTTP_200_OK)
            return Response({keys.SUCCESS:False,keys.MESSAGE:messages.ITEM_DOES_NOT_EXISTS},status=status.HTTP_400_BAD_REQUEST)
        return Response({keys.SUCCESS:False,keys.MESSAGE:messages.ITEM_DOES_NOT_EXISTS},status=status.HTTP_400_BAD_REQUEST)
            

class GetAllItemsAPI(APIView):
    """API to retrieve Item Datas"""

    permission_classes = [IsAuthenticated]

    def get(self,request):
        item_queryset = cache.get('cached_all_queryset')

        item_queryset = item_models.ItemsData.objects.all()
        serializer = item_serializers.ItemDataSerializer(item_queryset,many=True)
        cache.set('cached_all_queryset',serializer.data, timeout=60*60)
        return Response({keys.SUCCESS:True,keys.DATA:serializer.data},status=status.HTTP_200_OK)
                    
        
class UpdateItemAPI(APIView):
    """API to Update Item"""

    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        request_data = request.data.copy()
        item_queryset = item_models.ItemsData.objects.filter(id=id)

        if not item_queryset.exists():
            return Response({keys.SUCCESS: False, keys.MESSAGE: messages.ITEM_DOES_NOT_EXISTS}, status=status.HTTP_404_NOT_FOUND)

        item_instance = item_queryset.first()
        serializer = item_serializers.ItemDataSerializer(item_instance, data=request_data, partial=True)

        if serializer.is_valid():
            serializer.save()
            cache.set('cached_queryset', serializer.data, timeout=60*60)
            cache.delete('cached_all_queryset')
            return Response({keys.SUCCESS: True, keys.DATA: serializer.data}, status=status.HTTP_200_OK)

        return Response({keys.SUCCESS: False, keys.MESSAGE: serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

 
class DeleteItemAPI(APIView):
    """API to Delete Item"""

    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        try:
            item_instance = item_models.ItemsData.objects.get(id=id)
            item_instance.delete()
            cache.delete('cached_queryset')
            cache.delete('cached_all_queryset')
            return Response({keys.SUCCESS: True, keys.MESSAGE: messages.ITEM_DELETED}, status=status.HTTP_204_NO_CONTENT)
        except item_models.ItemsData.DoesNotExist:
            return Response({keys.SUCCESS: False, keys.MESSAGE: messages.ITEM_DOES_NOT_EXISTS}, status=status.HTTP_404_NOT_FOUND)


