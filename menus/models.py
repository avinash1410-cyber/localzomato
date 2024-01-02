from django.db import models
from django.contrib.auth.models import User
from restaurants.models import Restaurants
from django.utils import timezone



# Create your models here.
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    restaurants=models.ForeignKey(Restaurants,on_delete=models.CASCADE)
    content=models.TextField(max_length=100,null=True,blank=True)
    name=models.CharField(max_length=50,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=False, default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_content(self):
        return self.content.split(",")