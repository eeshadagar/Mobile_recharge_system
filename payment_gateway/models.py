from django.db import models

# Create your models here.

class Payments_pre(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=40,null=True, blank=True)
    number = models.IntegerField(null=True)
    expiry = models.IntegerField(null=True, blank=True)
    cvv = models.IntegerField(null=True, blank=True)

class Payments_post(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=40,null=True, blank=True)
    number = models.IntegerField(null=True)
    expiry = models.IntegerField(null=True, blank=True)
    cvv = models.IntegerField(null=True, blank=True)
