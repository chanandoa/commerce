from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.category}"

class Listing(models.Model):
    owner = models.CharField(max_length=64)
    title = models.CharField(max_length=64, unique=True)
    description = models.TextField(max_length=500)
    price = models.IntegerField(default = 0)
    image = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    bids = models.ManyToManyField('Bid', blank=True, related_name='listing_bid')

    def __str__(self):
        return f"{self.id}: {self.title}"

class Bid(models.Model):
    bidder = models.CharField(max_length=64)
    bid = models.IntegerField()
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}: {self.bid}, {self.listing}"
