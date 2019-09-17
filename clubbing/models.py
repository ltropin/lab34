from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    BUYER = 'BR'
    ORGANIZER = 'OR'
    GROUP_CHOICE = [
        (BUYER, 'Buyer'),
        (ORGANIZER, 'Organizer')
    ]
    group = models.CharField(max_length=2, choices=GROUP_CHOICE, default=BUYER)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class Purchase(models.Model):
    OPEN = 'OP'
    CLOSED = 'CL'
    SELL = 'SL'
    STATUS_CHOICE = [
        (OPEN, 'Open'),
        (CLOSED, 'Closed'),
        (SELL, 'Sell')
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS_CHOICE, default=OPEN)
    max_cost = models.IntegerField()


class Item(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    img = models.CharField(max_length=1000, default='')
    decription = models.TextField(default='')


class Orders(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)