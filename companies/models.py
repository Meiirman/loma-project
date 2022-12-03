from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=50,default="Новый город", blank=False)
    description = models.CharField(max_length=1500, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return self.name
    
