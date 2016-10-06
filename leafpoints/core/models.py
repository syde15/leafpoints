from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    point_total = models.IntegerField()
    user_name = models.CharField(max_length=30)

class Partner(models.Model):
    name = models.CharField(max_length=60)
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    partner = models.ForeignKey(Partner)
    points = models.IntegerField()
    thumbnail = models.URLField(null=True)
    backlink = models.URLField(null=True)
    description = models.URLField(max_length=1000, null=True)

class Transaction(models.Model):
    user = models.ForeignKey(Users)
    date = models.DateField()
    product = models.ForeignKey(Product)

class WaterSavings(models.Model):
    product = models.ForeignKey(Product)
    water_saved = models.DecimalField(max_digits=8, decimal_places=2)
    daily_savings = models.BooleanField()
    product_life = models.IntegerField()
