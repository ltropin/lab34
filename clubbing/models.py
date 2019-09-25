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
    avatar = models.ImageField(default='avatars/none.png', upload_to='avatars', unique=True)
    group = models.CharField(max_length=2, choices=GROUP_CHOICE, default=BUYER)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
    
    def get_orders(self):
        return Order.objects.filter(buyer=self)


class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    img = models.CharField(max_length=1000, default='')
    decription = models.TextField(default='')

    def get_all(self):
        data = [(ix, el) for ix, el in Item.objects.all()]
        return data


    def __str__(self):
        return self.name

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
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    
    status = models.CharField(max_length=2, choices=STATUS_CHOICE, default=OPEN)
    max_cost = models.BigIntegerField()
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Order', through_fields=('purchase', 'buyer'), related_name='members_purchase')
    
    def __str__(self):
        return f"ID: {self.id}, Item: {self.item}"

class Order(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"Purchase: {self.purchase}, Buyer: {self.buyer}"