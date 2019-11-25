from django.db import models

class Account(models.Model):
    account_number = models.CharField(max_length = 4)
    account_name = models.CharField(max_length = 100)

