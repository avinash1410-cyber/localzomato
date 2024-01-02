from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Restaurants(models.Model):
    VEG = 'Veg'
    NON_VEG = 'NonVeg'
    BOTH = 'Both'

    CATEGORY_CHOICES = [
        (VEG, 'Veg'),
        (NON_VEG, 'NonVeg'),
        (BOTH, 'Both'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, db_index=True)
    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        null=True,
        blank=True,
        db_index=True,
    )
    contact_info = models.CharField(max_length=100, null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=False, default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
