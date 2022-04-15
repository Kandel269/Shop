from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 100)
    describe = models.TextField(blank = True )
    price = models.DecimalField(max_digits = 12, decimal_places = 2)
    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

class Producer(models.Model):
    name = models.CharField(max_length = 100)
    describe = models.TextField(blank = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Producer"
        verbose_name_plural = "Producers"