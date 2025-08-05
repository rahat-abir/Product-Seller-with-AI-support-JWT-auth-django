from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Gaming', 'Gaming'),
        ('Audio', 'Audio'),
        ('Office', 'Office'),
        ('Accessories', 'Accessories'),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Accessories')
    image = models.CharField(max_length=100, default='fas fa-box')  # Font Awesome icon
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=4.0)
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
