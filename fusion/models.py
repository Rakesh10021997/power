from django.db import models

# Create your models here.
class Dress(models.Model):
    dressname=models.CharField(max_length=30,null=True, default='')
    rent_price=models.IntegerField()
    rent_security=models.IntegerField()
    size=models.CharField(max_length=30,null=True, default='')
    product_name=models.CharField(max_length=30,null=True, default='')
    product_id=models.CharField(max_length=30,null=True, default='')
    color=models.CharField(max_length=30,null=True, default='')
    materials=models.CharField(max_length=30,null=True, default='')
    neckdesign=models.CharField(max_length=30,null=True, default='')
    sleeves=models.CharField(max_length=30,null=True, default='')
    designer=models.CharField(max_length=30,null=True, default='')
   
