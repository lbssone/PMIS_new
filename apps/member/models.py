from django.db import models

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