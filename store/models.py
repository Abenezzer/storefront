from django.db import models

# Create your models here.

class Collection(models.Model):
    title = models.CharField(max_length=255)


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.PositiveIntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)

    MEMBERSHIP_DEFAULT_CHOICE = 'B'
    MEMBERSHIP_CHOICES  = [
        (MEMBERSHIP_DEFAULT_CHOICE, 'Bronz'),
        ('S', 'Silver'),
        ('G', 'Gold')
    ]

    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_DEFAULT_CHOICE)


class Adress(models.Model):
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)

class Order(models.Model):
    placed_at = models.DateTimeField(auto_now=True)

    PAYMENT_STATUS_DEFAULT_CHOICE = 'P'

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_DEFAULT_CHOICE, 'Pending'),
        ('C', 'Complete'),
        ('F', 'Field')
    ]
    payment_status = models.CharField(max_length=1, choices= PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_DEFAULT_CHOICE)


