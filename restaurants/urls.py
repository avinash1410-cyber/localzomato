from django.urls import path
from .views import *


urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('about/',About),
    path('login/', custom_login, name='custom_login'),
    path('logout/', custom_logout, name='custom_logout'),
    path('contact/',Contact),
    path('restaurant_list/', RestaurantListView.as_view(), name='restaurant_list'),
    path('restaurant_list/<slug:slug>/', RestaurantListView.as_view(), name='restaurant_list'),
    path('restaurants/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant_detail'),
    path('add/', add_restaurant, name='add_restaurant'),
    # path('create/', AddRestaurantView2.as_view(), name='create_restaurant'),
]
