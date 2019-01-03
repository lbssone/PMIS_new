from django.contrib import admin

from .models import Member, Transaction, Transaction_product

# Register your models here.
admin.site.register(Member)
admin.site.register(Transaction)
admin.site.register(Transaction_product)
