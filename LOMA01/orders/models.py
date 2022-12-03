from django.db import models

# Create your models here.
from datetime import datetime
from email.policy import default
from pickle import TRUE
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User
from colorfield.fields import ColorField
from companies.models import Company
from couriers.models import Courier
from django.utils.translation import gettext_lazy as _

from users.models import LomaUser

# Create your models here.


class Stage(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="Новый этап")
    color = ColorField(default='#2d4bf0')
    is_main_stage = models.BooleanField(default=False)
    # company = models.ForeignKey("companies.Company", verbose_name=_("Company"), on_delete=models.CASCADE, blank=True)
    class Meta:
        managed = True
        db_table = 'stages'
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50, default="Новый Продукт")
    among = models.IntegerField(default=0, blank=False)
    price_per_piece = models.FloatField(default=0.00, blank=False)
    company = models.ForeignKey("companies.Company", verbose_name=_("Company"), on_delete=models.CASCADE, blank=True, null=True)
            
    def __str__(self):
        return str(self.name) + " (" + str(self.among) + ")"

class Order(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000,blank=True, default='' )
    address = models.CharField(max_length=1000,blank=True, default='' )
    create_date = models.DateTimeField(default=datetime.now())
    change_date = models.DateTimeField(default=datetime.now())
    creator = models.ForeignKey(LomaUser,on_delete=models.SET_NULL,null=True,related_name='creator_%(model_name)s',)    
    stage = models.ForeignKey(Stage, db_column="stages",on_delete=models.CASCADE)
    responsible = models.ForeignKey(LomaUser,on_delete=models.SET_NULL,null=True,related_name='responsible_%(model_name)s')
    courier = models.ForeignKey(Courier,on_delete=models.SET_NULL,null=True,related_name='responsible_%(model_name)s')
    orders_product = models.CharField(max_length=1,blank=True,default='')
    product_list = models.CharField(max_length=1,blank=True,default='') 
    product = models.ForeignKey(Product, db_column="product",on_delete=models.CASCADE) 
    budget = models.FloatField(default=0.00, blank=True)
    delivery_date = models.DateTimeField(default=datetime.now())
    message_sended = models.BooleanField(default=False)
    source = models.CharField(max_length=250, default="Создан вручную", blank=True)
    company = models.ForeignKey(Company, verbose_name=_("Company"), on_delete=models.SET_NULL, blank=True, null=True, related_name='company_%(model_name)s')
    client_FIO = models.CharField(max_length=1000,blank=True, default='' )
    client_phone = models.CharField(max_length=1000,blank=True, default='' )
        
    def __str__(self):
        return self.name

