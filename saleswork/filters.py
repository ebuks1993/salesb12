from dataclasses import fields
from django_filters.rest_framework import FilterSet
from .models import Collection,PrevCollection,current,Previous


class PrevCollectionFilter(FilterSet):
    class Meta:
        model=PrevCollection
        fields = {
            'Date':['gte','lte'],
           
        }


class CollectionFilter(FilterSet):
    class Meta:
        model=Collection
        fields = {
            'Date':['gte','lte'],
           
        }


class currentFilter(FilterSet):
    class Meta:
        model=current
        fields = {
            'TEAM':['exact'],
            'Date':['gte','lte'],
            'pro':['exact']
        }



class PreviousFilter(FilterSet):
    class Meta:
        model=Previous
        fields = {

            'TEAM':['exact'],
            'Date':['gte','lte'],
            'pro':['exact']
        }
