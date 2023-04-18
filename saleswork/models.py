from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email=models.EmailField(unique=True)


    
class Semibase (models.Model):
    status1=(
        ('Trade','Trade'),
        ('Marketing','Marketing')
        )
    cond1=(
        ('Active','Active'),
        ('Inactive','Inactive')
        )

    NSM = models.CharField( max_length=550)
    RSM = models.CharField( max_length=550)
    ASM = models.CharField( max_length=550)
    REP = models.CharField( max_length=550 , default='null')
    REGION = models.CharField( max_length=550)
    CHANNEL = models.CharField( max_length=550)
    GROUP = models.CharField( max_length=3550)
    TEAM = models.CharField( max_length=550)
    # CODE = models.CharField(max_length=450)
    STATUS = models.CharField( max_length=550)
    SEGMENT= models.CharField( max_length=150, choices=status1 ,default='Marketing')
    condition= models.CharField( max_length=150, choices=cond1 ,default='Active')

    def __str__(self):
        return self.GROUP

class Ledgerbase(models.Model):
    semi=models.ForeignKey(Semibase,on_delete=models.DO_NOTHING)
    LEDGER = models.CharField( max_length=1500)
    TEAM = models.CharField( max_length=1500)
    STATUS = models.CharField( max_length=1500)
    GROUP = models.CharField( max_length=1500)

    class Meta:
        unique_together= ('semi','LEDGER','TEAM','STATUS','GROUP')

class Product(models.Model):
    Name = models.CharField(max_length=1500)
    Price = models.IntegerField()
    ctnqty = models.IntegerField(default=0)

    def __str__(self):
        return self.Name

class Budget (models.Model):
    procode = models.ForeignKey(Product, on_delete=models.CASCADE)
    GROUP = models.CharField( max_length=500)
    TEAM = models.CharField( max_length=500)
    semi = models.ForeignKey(Semibase, on_delete=models.CASCADE)
    Product = models.CharField( max_length=500)
    # value = models.IntegerField()
    value = models.DecimalField(max_digits=10 ,decimal_places=3,null=True)
   
class current (models.Model):
    pro = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    cust = models.ForeignKey(Ledgerbase, on_delete=models.DO_NOTHING)
    Date = models.DateField()
    Money = models.IntegerField()
    TEAM = models.CharField( max_length=500)
    product = models.CharField( max_length=1500)
    customers = models.CharField( max_length=500)
    month = models.IntegerField()
    ctns = models.IntegerField()
    # fyear = models.IntegerField()
    fyear = models.DecimalField(max_digits=10 ,decimal_places=3,null=True)

    # class Meta:
    #     unique_together=['pro','cust','fyear','TEAM','product','customers','month','ctns']


class Previous (models.Model):
    pro = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    cust = models.ForeignKey(Ledgerbase, on_delete=models.DO_NOTHING)
    Date = models.DateField()
    Money = models.IntegerField()
    TEAM = models.CharField( max_length=500)
    product = models.CharField( max_length=1500)
    customers = models.CharField( max_length=500)
    month = models.IntegerField()
    ctns = models.IntegerField()
    fyear = models.IntegerField()


    # class Meta:
    #     unique_together=['pro','cust','fyear','TEAM','product','customers','month','ctns']

class month(models.Model):
    status=(
        ('Active','Active'),
        ('Inactive','Inactive')
        )
    month = models.CharField( max_length=450)
    pointer = models.IntegerField()
    fullstatus = models.CharField( max_length=150, choices=status ,default='Inactive')


class year(models.Model):
    status=(
        ('Active','Active'),
        ('Inactive','Inactive')
        )
    year = models.IntegerField()
    pointer = models.IntegerField()
    fullstatus = models.CharField(max_length=150, choices=status ,default='Inactive')


class Collection (models.Model):
    cust = models.ForeignKey(Ledgerbase, on_delete=models.DO_NOTHING)
    Date = models.DateField()
    Name = models.CharField( max_length=500)
    Amount = models.IntegerField()
    month = models.CharField( max_length=50 ,null=True)
    fyear = models.IntegerField()

class PrevCollection (models.Model):
    cust = models.ForeignKey(Ledgerbase, on_delete=models.DO_NOTHING)
    Date = models.DateField()
    Name = models.CharField( max_length=500)
    Amount = models.IntegerField()
    month = models.CharField( max_length=50 ,null=True)
    fyear = models.IntegerField()


class Period(models.Model):
    Opening = models.DateField()
    Closing = models.DateField()