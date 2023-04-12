from django.contrib import admin
from .models import Semibase ,Ledgerbase,Product,Budget,month,year,Collection,PrevCollection,Period,current,Previous,User
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(User)
class Useradmin(BaseUserAdmin):
    # list_display = ['id','username','first_name','last_name']
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username","email","password1", "password2","first_name")
            },
        ),
    )


# Register your models here.
class salesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['id','NSM','RSM','ASM','REP','REGION','TEAM','GROUP','STATUS','CHANNEL','SEGMENT']
    search_fields=['GROUP__icontains']
    ...

admin.site.register(Semibase,salesAdmin)

# @admin.register(Semibase)
# class Salesadmin
class salesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['id','semi','LEDGER','TEAM','STATUS','GROUP']
    search_fields=['LEDGER__icontains']
    ...

admin.site.register(Ledgerbase,salesAdmin)


class salesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['id','Name','Price']
    search_fields=['Name__icontains']
    ...

admin.site.register(Product,salesAdmin)


class salesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['id','procode','GROUP','TEAM','semi','Product','value']
    search_fields=['Product__icontains','GROUP__icontains']
    ...

admin.site.register(Budget,salesAdmin)


class salesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['id','Date','customers','product','TEAM','ctns','Money','fyear']
    search_fields=['customers__icontains',]
    ...

admin.site.register(current,salesAdmin)

class PreviousAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['id','Date','customers','product','TEAM','ctns','Money','fyear']
    search_fields=['customers__icontains',]
    ...

admin.site.register(Previous,PreviousAdmin)


class MonthAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['id','month','pointer','fullstatus']
    
    ...

admin.site.register(month,MonthAdmin)


class MonthAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['id','year','pointer','fullstatus']
    
    ...

admin.site.register(year,MonthAdmin)


class CollectionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['id','Date','cust_id','Name','Amount','fyear']
    
    ...

admin.site.register(Collection,CollectionAdmin)



class PrevcollectionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['id','Date','cust_id','Name','Amount','fyear']
    
    ...

admin.site.register(PrevCollection,PrevcollectionAdmin)



class PeriodAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['id','Opening','Closing']
    
    ...

admin.site.register(Period,PeriodAdmin)