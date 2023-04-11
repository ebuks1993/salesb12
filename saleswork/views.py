from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Semibase,Product,Budget,Ledgerbase,month,year,Collection,PrevCollection,Period,current,Previous
from .Serializer import SemiSerializer,ProductSerializer,BudgetSerializer,LedgerSerializer,Monthserializer,Yearserializer,Collectionserializer,PrevCollectionserializer,PeriodSerializer,CurrentSerializer,PreviousSerializer
from .pagination import DefaultPagination
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models.aggregates import Count,Sum,Min,Max,Avg
from .filters import CollectionFilter,PrevCollectionFilter,currentFilter,PreviousFilter


# Create your views here.


class CurrentViewset(ModelViewSet):
    queryset=current.objects.select_related('cust').all()
    serializer_class=CurrentSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_class=currentFilter

#     serializer_class=CurrentSerializer

#     # pagination_class=DefaultPagination

class PreviousViewset(ModelViewSet):
    queryset=Previous.objects.select_related('cust').all()
    serializer_class=PreviousSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_class=PreviousFilter


class SemiViewset(ModelViewSet):
    queryset=Semibase.objects.prefetch_related('ledgerbase_set').all()
    serializer_class=SemiSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['REGION','CHANNEL','TEAM','ASM','REP','SEGMENT']

class ProductViewset(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class BudgetViewset(ModelViewSet):
    queryset=Budget.objects.select_related('procode').all()
    serializer_class=BudgetSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['procode','TEAM']

class LedgerViewset(ModelViewSet):
    queryset=Ledgerbase.objects.select_related('semi').all()
    serializer_class=LedgerSerializer
    


class MonthViewset(ModelViewSet):
    queryset=month.objects.all()
    serializer_class=Monthserializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['fullstatus']


class YearViewset(ModelViewSet):
    queryset=year.objects.all()
    serializer_class=Yearserializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['fullstatus']

class CollectionViewset(ModelViewSet):
    queryset=Collection.objects.select_related('cust').all()
    serializer_class=Collectionserializer
    filter_backends=[DjangoFilterBackend]
    filterset_class=CollectionFilter

class PrevCollectionViewset(ModelViewSet):
    queryset=PrevCollection.objects.select_related('cust').all()
    serializer_class=PrevCollectionserializer
    filter_backends=[DjangoFilterBackend]
    filterset_class=PrevCollectionFilter

class periodviewset(ModelViewSet):
    queryset=Period.objects.all()
    serializer_class=PeriodSerializer

