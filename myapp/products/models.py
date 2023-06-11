from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    type = models.CharField(max_length=50)
