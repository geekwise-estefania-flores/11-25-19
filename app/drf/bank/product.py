from django.db import models

class Product(models.Model):
    product_options = (
        ('savings', 'SAVINGS'), 
        ('checking', 'CHECKING'), 
        ('credit', 'CREDIT'), 
        ('debit', 'DEBIT')
    )

    product = models.CharField(
        max_length = 8, 
        choices = product_options,
        default =product_options[0]
    )