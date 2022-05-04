from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator, MaxLengthValidator, MinValueValidator
from django.utils.translation import activate

#from shop.models import Product

class Voucher(models.Model):
    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField()
    #product = models.ForeignKey(Product, default='822e2e7686134e5289fe9e1d4d3e4770', on_delete=models.CASCADE)
def __str__(self):
    return self.code
