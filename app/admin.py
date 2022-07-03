from django.contrib import admin
from .models import (
    Customer,
    Tour,
    Cart,
    Booked,
    Train
)

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'locality', 'city', 'zipcode', 'state']

@admin.register(Tour)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'city', 'original_price', 'discounted_price', 'description', 'product_image',]

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'tour', 'quantity']

@admin.register(Booked)
class BookedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'tour', 'quantity', 'ordered_date', 'status']

@admin.register(Train)
class TrainModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'train_no', 'train_name', 'train_from', 'train_to', 'train_time', 'train_price']
    