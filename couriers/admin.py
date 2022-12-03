from django.contrib import admin



# Register your models here.
from .models import *


@admin.register(Courier)
class Courier(admin.ModelAdmin):
    list_display = (
        'name',
        'surname',
        'phone_number',
        'telegram_name',
        # 'available_regions',
        'telegram_chat_id',
        'isActive',
    )


@admin.register(Region)
class Region(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )

