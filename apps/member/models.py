from django.db import models
from django.db.models import Sum
from apps.inventory.models import Product

# Create your models here.
class Member(models.Model):
    member_name = models.CharField(max_length=20, null=True)
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




