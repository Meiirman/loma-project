from django.contrib import admin

from django.contrib.auth.models import User
from django.contrib.auth.models import Group


# admin.site.unregister(User)
admin.site.unregister(Group)



# Register your models here.
from .models import *


@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'address',
        'create_date',
        'change_date',
        'creator',
        'stage',
        'responsible',
        'courier',
        'orders_product',
        'product_list',
        'product',
        'budget',
        'delivery_date',
        'message_sended',
        'source',
        'company',
        'client_FIO',
        'client_phone',
    )

@admin.register(Stage)
class Client(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'color',
    )    
    list_editable = (
        'color',
    )

