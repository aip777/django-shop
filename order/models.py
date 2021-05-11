from django.db import models
from customer.models import Customer
from product.models import Products
from django.utils.timezone import now

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Customer')
    products    = models.ManyToManyField(Products, blank=False)
    # unit_price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    # quantity = models.IntegerField(blank=False)
    # amount = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    # # @property
    # def check_quantity(self):
    #     if self.products:
    #         print(self.products)
        
    #     return self.products

    def __str__(self):
        return str(self.customer)