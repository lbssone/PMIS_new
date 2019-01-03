from django.db import models
from django.db.models import Sum
from apps.inventory.models import Product

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    AGE=(
        ('0-17','17歲以下'),
        ('18-30','18-30歲'),
        ('31-40','31-40歲'),
        ('41-50','41-50歲'),
        ('51','51歲以上'),
    )
    age = models.CharField(max_length=10, choices=AGE, default="18-30")
    GENDER=(
        ('F','女性'),
        ('M','男性'),
    )
    gender = models.CharField(max_length=10, choices=GENDER, default="F")
    cellphone_number = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(unique=True, null=True)
    DWELLING=(
        ('N','台灣北部'),
        ('M','台灣中部'),
        ('S','台灣南部'),
        ('E','台灣東部'),
        ('O','其他'),
    )
    dwelling = models.CharField(max_length=10, choices=DWELLING, default="N")

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @property
    def name(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Transaction(models.Model):
    member = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    total_price = models.PositiveIntegerField(null=True, blank=True)
    products = models.ManyToManyField(Product, through='Transaction_product')

    def __str__(self):
        return '{} {}'.format(self.member.name, str(self.date))

    @staticmethod
    def calculate_total_price(self):
        t_price = 0
        for tran in self.transaction_product_set.all():
            t_price += tran.price
        return t_price
        # return self.product.all().aggregate(total_price=Sum('price'))['total_price']

    def save(self, *args, **kwargs):
        try:
            self.total_price = Transaction.calculate_total_price(self)
        except:
            self.total_price = 0
        super(Transaction, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-date"] 

class Transaction_product(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=True)
    price = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.transaction.member.name + " " + self.product.name
    
    def save(self, *args, **kwargs):
        self.price = self.product.price * self.quantity
        super(Transaction_product, self).save(*args, **kwargs)


class Activity(models.Model):
    activity_name = models.CharField(max_length=20, blank=True)
    target_name = models.CharField(max_length=50, null=True)
    activity_date = models.DateField(null=True)
    target = models.IntegerField(blank=True)
    response = models.IntegerField(blank=True)
    cost = models.IntegerField(blank=True)

    #select more than one member
    target_members = models.ManyToManyField(Member, blank=True)

    #獲取率
    def get(self):
        try:
            get = round(self.response / self.target,2)
        except ZeroDivisionError:
            get = 0
        return get
    
    #取得成本
    def efficiency(self):
        try:
            efficiency = round(self.cost / self.response,2)
        except ZeroDivisionError:
            efficiency = 0
        return efficiency

    def __str__(self):
        return self.activity_name
    
    class Meta:
        ordering = ["-activity_date"]