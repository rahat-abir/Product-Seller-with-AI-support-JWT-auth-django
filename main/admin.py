from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'rating', 'stock', 'created_at']
    list_filter = ['category', 'rating', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['price', 'stock', 'rating']
    ordering = ['-created_at']
