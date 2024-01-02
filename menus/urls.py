from django.urls import path
from .views import *


urlpatterns = [
    path('item_list/', ItemListView.as_view(), name='item_list'),
    path('item_list/<slug:slug>/', ItemListView.as_view(), name='item_list'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    path('add/', AddItemView.as_view(), name='add_item'),
]
