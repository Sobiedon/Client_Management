from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Vehicle(models.Model):
    customer_name = models.CharField(max_length=50, blank=False, null=False, default=' ')
    vehicle_make = models.CharField(max_length=50, blank=False, null=False, default=' ')
    model = models.CharField(max_length=10, blank=True, null=True, default=' ')
    VIN_number = models.CharField(max_length=30, default='00000')
    date_of_purchase = models.DateTimeField()
    date_of_last_Service = models.DateTimeField()
    notes = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,

    )

    def __str__(self):
        return self.vehicle_make

    def get_absolute_url(self):
        return reverse('client_detail', args=[str(self.id)])
