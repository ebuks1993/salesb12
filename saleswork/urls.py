from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views

router=DefaultRouter()
router.register('current', views.CurrentViewset, basename='current')
router.register('Previous', views.PreviousViewset, basename='Previous')

router.register('semi', views.SemiViewset, basename='semi')
router.register('Product', views.ProductViewset, basename='Product')
router.register('Budget', views.BudgetViewset, basename='Budget')
router.register('Ledger', views.LedgerViewset, basename='Ledger')
router.register('Month', views.MonthViewset, basename='Month')
router.register('Year', views.YearViewset, basename='Year')
router.register('collection', views.CollectionViewset, basename='collection')
router.register('Prevcollection', views.PrevCollectionViewset, basename='Prevcollection')
router.register('period', views.periodviewset, basename='period')

urlpatterns = [
    path("",include(router.urls)),
    ]
