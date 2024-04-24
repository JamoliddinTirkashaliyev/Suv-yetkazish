from django.shortcuts import get_object_or_404
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.pagination import *
from rest_framework.pagination import PageNumberPagination


class MyCustomPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100

class SuvlarModelViewSet(ModelViewSet):
    queryset = Suv.objects.all()
    serializer_class = SuvSerializers

class MijozlarModelViewSet(ModelViewSet):
    queryset = Mijoz.objects.all()
    serializer_class = MijozSerializers

    filter_backends = [filters.SearchFilter]
    search_fields = ['ism', 'tel']

class BuyurtmalarModelViewSet(ModelViewSet):
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializers

class AdminlarModelViewSet(ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializers

class HaydovchilarModelViewSet(ModelViewSet):
    queryset = Haydovchi.objects.all()
    serializer_class = SuvSerializers