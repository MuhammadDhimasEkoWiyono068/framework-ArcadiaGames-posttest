from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Users(models.Model):
    CUSTOMER = 1
    ADMIN = 2
    ROLE_CHOICES = (
        (CUSTOMER, 'Customer'),
        (ADMIN, 'Admin'),
    )
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    role = models.IntegerField(choices=ROLE_CHOICES, default=CUSTOMER)  # 1 = Customer, 2 = Admin
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.username
