from email.policy import default
import imp
from pyexpat import model
from tokenize import blank_re
from unicodedata import name
from django.db import models
from companies.models import Region
from django.utils.translation import gettext_lazy as _

class Courier(models.Model):
    name = models.CharField(max_length=50, default='New Courier')
    surname = models.CharField(max_length=50, blank=True, default='')
    telegram_chat_id = models.IntegerField(default=0)
    available_regions = models.ManyToManyField("companies.Region", verbose_name=_("Regions"),blank=True, default={})
    isActive = models.BooleanField(default=False) 
    telegram_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50, blank=True)
    company = models.ForeignKey("companies.Company", verbose_name=_("Company"), on_delete=models.CASCADE, blank=True)
    
    def __str__(self) -> str:
        return self.telegram_name

    
