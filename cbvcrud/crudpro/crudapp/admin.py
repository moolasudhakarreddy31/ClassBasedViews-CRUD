from django.contrib import admin
from crudapp.models import Company


# Register your models here.

class CampanyAdmin(admin.ModelAdmin):
    list_display=['name','ceo','location']

admin.site.register(Company,CampanyAdmin)












