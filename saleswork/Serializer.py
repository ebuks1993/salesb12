from rest_framework import serializers 
from .models import Semibase,Product,Budget,Ledgerbase,month,year,Collection,PrevCollection,Period,current,Previous
from django.db.models.aggregates import Count,Sum,Min,Max,Avg


class LedgerSerializer(serializers.ModelSerializer):
    reg=serializers.SerializerMethodField(method_name='region')
    class Meta:
        model=Ledgerbase
        fields=['id','semi','TEAM','STATUS','GROUP','LEDGER','reg']


    def region(self , leg:Ledgerbase):
        return leg.semi.REGION

class CurrentSerializer(serializers.ModelSerializer):
    semi=serializers.SerializerMethodField(method_name='sem')
    # cust=LedgerSerializer()
    class Meta:
        model=current
        fields=['id','pro','cust','Date','Money','TEAM','product','customers','month','ctns','fyear','semi']


    def sem(self , curr:current):
        return curr.cust.semi_id

class PreviousSerializer(serializers.ModelSerializer):
    semi=serializers.SerializerMethodField(method_name='sem')
    # cust=LedgerSerializer()
    class Meta:
        model=Previous
        fields=['id','pro','cust','Date','Money','TEAM','product','customers','month','ctns','fyear','semi']


    def sem(self , prev:Previous):
        return prev.cust.semi_id

class SemiSerializer(serializers.ModelSerializer):
    # trial=serializers.SerializerMethodField(method_name='cursales')
    # Lasttrial=serializers.SerializerMethodField(method_name='lastsales')
   
    class Meta:
        model=Semibase
        fields=['id','NSM','RSM','ASM','REP','REGION','CHANNEL','GROUP','TEAM','STATUS',]



class ProductSerializer(serializers.ModelSerializer):
    # bud=serializers.SerializerMethodField(method_name='prodbudget')
    # fud=serializers.SerializerMethodField(method_name='revenue')
    class Meta:
        model=Product
        fields=['id','Name','Price','ctnqty']
    
    # def prodbudget (self ,prod:Product):
    #     bad=0
    #     cow=[]
    #     mow=0
    #     for i in prod.budget_set.all():
    #         # bad=(current.objects.filter(cust=i,fyear=2022).aggregate(totalsales=Sum('Money'))) 
    #         cow.append(i.value ) 
    #         mow=sum(cow) 
                            
    #     return mow

    # def revenue (self ,prod:Product):
    #     bad=0
    #     cow=[]
    #     mow=0
    #     for i in prod.budget_set.all():
    #         # bad=(current.objects.filter(cust=i,fyear=2022).aggregate(totalsales=Sum('Money'))) 
    #         cow.append(i.value * i.procode.Price ) 
    #         mow=sum(cow) 
                            
    #     return mow

    
        
class BudgetSerializer(serializers.ModelSerializer):

    buz=serializers.SerializerMethodField(method_name='rev')
    class Meta:
        model=Budget
        fields=['procode','GROUP','TEAM','semi','Product','value','buz']


    def rev(self,bud:Budget):
        return bud.value * bud.procode.Price



    
    

class Monthserializer(serializers.ModelSerializer):

     class Meta:
        model=month
        fields=['id','month','pointer','fullstatus']

    
    

class Yearserializer(serializers.ModelSerializer):
     class Meta:
        model=year
        fields=['id','year','pointer','fullstatus']


class Collectionserializer(serializers.ModelSerializer):
    semi=serializers.SerializerMethodField(method_name='sem')
    TEAM =serializers.SerializerMethodField(method_name='team')
    class Meta:
        model=Collection
        fields=['id','cust','Date','Name','Amount','month','fyear','TEAM','semi']


    def team(self,col:Collection):
        return  col.cust.TEAM
    

    def sem(self , col:Collection):
        return col.cust.semi_id


class PrevCollectionserializer(serializers.ModelSerializer):
    semi=serializers.SerializerMethodField(method_name='sem')
    TEAM =serializers.SerializerMethodField(method_name='team')
    class Meta:
        model=PrevCollection
        fields=['id','cust','Date','Name','Amount','month','fyear','TEAM','semi']


    def team(self,pcol:PrevCollection):
        return  pcol.cust.TEAM
    

    def sem(self , pcol:PrevCollection):
        return pcol.cust.semi_id



class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model=Period
        fields='__all__'