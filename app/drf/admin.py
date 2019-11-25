from django.contrib import admin
from bank import Account, Customer, Product

admin.site.register((
    Account,
    Customer, 
    Product
))
