from django.db import models
from django.contrib.auth.models import User


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='vendor', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
