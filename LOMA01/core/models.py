from django.db import models

from users.models import LomaUser


class CustomBackground(models.Model):
    user = models.ForeignKey(LomaUser,on_delete=models.SET_NULL,null=True,related_name='responsible_%(model_name)s')
    background = models.ImageField(upload_to='static')
