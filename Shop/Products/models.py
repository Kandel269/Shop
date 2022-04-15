from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 100)
    describe = models.TextField(blank = True )
    price = models.DecimalField(max_digits = 12, decimal_places = 2)