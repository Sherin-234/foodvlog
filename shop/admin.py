from django.contrib import admin
from .models import Category
from .models import products
# Register your models here.

class categAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
admin.site.register(Category,categAdmin)


class proAdmin(admin.ModelAdmin):
    list_display=['name','price','img','stock']
    list_editable=['price','stock','img']
    prepopulated_fields={'slug':('name',)}
admin.site.register(products,proAdmin)