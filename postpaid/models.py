from django.db import models

# Create your models here.

class postrecharge(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField(max_length=15, default=78291300)
    operator = models.CharField(max_length=15)
    region = models.CharField(max_length=15)
