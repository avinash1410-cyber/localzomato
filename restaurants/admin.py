from django.contrib import admin
from .models import Restaurants

class RestaurantsAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'category', 'created_at', 'updated')
    search_fields = ('name', 'location', 'category')
    list_filter = ('category', 'location')
    date_hierarchy = 'created_at'

# Associate the custom admin class with the Restaurants model
admin.site.register(Restaurants, RestaurantsAdmin)
