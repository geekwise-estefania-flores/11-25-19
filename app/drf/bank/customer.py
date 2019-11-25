from django.db import models

class Customer(models.Model):
    customer_first_name = models.CharField(max_length = 300)
    customer_last_name = models.CharField(max_length = 300)
    customer_phone_number = models.CharField(max_length = 15)
