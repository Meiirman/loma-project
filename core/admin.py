from django.contrib import admin
# Register your models here.
from .models import *


@admin.register(CustomBackground)
class CustomBackground(admin.ModelAdmin):
    list_display = (
        'user',
        'background',
    )
    list_editable = (
        # 'background',
    )

