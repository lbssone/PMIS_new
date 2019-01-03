from django.db import models
from django.db.models import Sum
from apps.inventory.models import Product

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    member_number = models.PositiveIntegerField(null=True)
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other')
    )
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
    )
    age = models.PositiveIntegerField(null=True)
    cellphone_number = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(unique=True, null=True)
    occupation = models.CharField(max_length=30, null=True)
    NORTHERN = '北部'
    CENTRAL = '中部'
    SOUTHERN = '南部'
    WESTERN = '東部'
    REGION_CHOICES = (
        (NORTHERN, '北部'),
        (CENTRAL, '中部'),
        (SOUTHERN, '南部'),
        (WESTERN, '東部')
    )
    working_school_address = models.CharField(
        max_length=50,
        choices=REGION_CHOICES,
        null=True,
    )
    home_address = models.CharField(
        max_length=50,
        choices=REGION_CHOICES,
        null=True,
    )

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @property
    def name(self):
        return '{} {}'.format(self.first_name, self.last_name)


# class Transaction(models.Model):
#     member = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
#     date = models.DateField(auto_now=False, auto_now_add=False, null=True)
#     products = models.ManyToManyField(Transaction_product, blank=True)
#     total_price = models.PositiveIntegerField(null=True, blank=True)

#     def __str__(self):
#         return self.member.name

#     @staticmethod
#     def calculate_total_price(self):
#         t_price = 0
#         for product in self.products.all():
#             t_price += product.price
#         return t_price
#         # return self.product.all().aggregate(total_price=Sum('price'))['total_price']

#     def save(self, *args, **kwargs):
#         self.total_price = Transaction.calculate_total_price(self)
#         super(Transaction, self).save(*args, **kwargs)

# class Transaction_product(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
#     price = models.PositiveIntegerField(null=True, blank=True)

#     def __str__(self):
#         return self.product.name
    
#     def save(self, *args, **kwargs):
#         self.price = self.product.price
#         super(Transaction_product, self).save(*args, **kwargs)