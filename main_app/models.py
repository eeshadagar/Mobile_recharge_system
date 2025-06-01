from django.db import models

# Create your models here.

class Detail(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    amount = models.IntegerField()
    operator = models.CharField(max_length=15)
