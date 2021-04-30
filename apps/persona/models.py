from django.contrib.auth.models import User
from django.db import models
from apps.product.models import Product
from django.conf import settings


class EventType(models.Model):
    event_type = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Event types"

    def __str__(self):
        return self.event_type


class Event(models.Model):
    event_creator = models.ForeignKey(User, default=User, on_delete=models.PROTECT)
    event_name = models.CharField(max_length=250)
    event_description = models.CharField(max_length=250)
    event_location = models.CharField(max_length=250)
    event_type = models.ForeignKey(EventType, related_name='type', on_delete=models.CASCADE)
    event_date = models.DateTimeField()
    event_cart = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Events"

    def __str__(self):
        return self.event_name
