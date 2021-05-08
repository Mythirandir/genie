from django.db import models
from apps.order.models import OrderItem
from datetime import datetime


class EventType(models.Model):
    event_type = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Event types"

    def __str__(self):
        return self.event_type


class Event(models.Model):
    event_name = models.CharField(max_length=250)
    event_description = models.CharField(max_length=250)
    event_location = models.CharField(max_length=250)
    event_type = models.ForeignKey(EventType, related_name='type', on_delete=models.CASCADE)
    event_date = models.DateTimeField(default=datetime.now())
    event_slug = models.SlugField(max_length=255, unique=True)
    event_cart = models.ForeignKey(OrderItem, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Events"

    def __str__(self):
        return self.event_name
