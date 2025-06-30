from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    stock_quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name