from django.db import models
from drf.product import Product
from drf.account import Account

class Customer(models.Model):
    customer_first_name = models.CharField(max_length = 300)
    customer_last_name = models.CharField(max_length = 300)
    customer_phone_number = models.CharField(max_length = 15)

    product = models.ForeignKey('auth.User', related_name='product', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product}'

    account = models.ForeignKey('auth.User', related_name='account', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.account}'

