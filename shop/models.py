
from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import render, get_object_or_404
#from .forms import CommentForm
from django.db import models
from django.db.models.fields import IntegerField
from django.urls import reverse
from django.conf import settings
from order.models import Order
#from phone_shop.settings import TIME_ZONE

from vouchers.models import Voucher


class Category(models.Model):
    id = models.IntegerField(
        primary_key=True,
        default=1,
        editable=False
    )
    name = models.CharField(default=None, max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('shop:product_by_category', args=[self.id])

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.IntegerField(
        primary_key=True,
        default=1,
        editable=False
    )

    name = models.TextField(max_length=25, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product', blank=True)
    stock = models.IntegerField()
    voucher = models.ForeignKey(Voucher, default=1, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    users_wishlist = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='user_wishlist', blank=True)
    #order = models.ForeignKey(Order, related_name='order_history', default=1, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_absolute_url(self):
        return reverse('shop:prod_detail', args=[self.category.id, self.id])

    def __str__(self):
        return self.name
