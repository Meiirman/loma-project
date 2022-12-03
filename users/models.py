from asyncio import proactor_events
from email.policy import default
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, UserManager



class Role(models.Model):
    name = models.CharField(max_length=50, default="Новый")

# Название доступов 
    update_settings = models.BooleanField(default=False)
    change_stage = models.BooleanField(default=False)
    update_orders = models.BooleanField(default=False)
    update_product_info = models.BooleanField(default=False)
    can_change_product_total_among = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name





class LomaUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.ForeignKey("users.Role", verbose_name=_("Role"), on_delete=models.CASCADE, blank=True)
    company = models.ForeignKey("companies.Company", verbose_name=_("Company"), on_delete=models.CASCADE, blank=True)


    def __str__(self) -> str:
        return self.user.username

    @property
    def get_accesse(self):
        access = {
            'update_settings': self.role.update_settings,
            'change_stage': self.role.change_stage,
            'update_orders': self.role.update_orders,
            'update_product_info': self.role.update_product_info,
            'can_change_product_total_among': self.role.can_change_product_total_among,
        }
        return access