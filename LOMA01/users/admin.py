from django.contrib import admin

from users.models import LomaUser, Role

# Register your models here.

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "update_settings",
        "change_stage",
        "update_orders",
        "update_product_info",
        "can_change_product_total_among",
    )
    


@admin.register(LomaUser)
class LomaUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
