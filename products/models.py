from django.db import models
from category.models import Category


class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True)  
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True) 
    image = models.ImageField(upload_to='products/product_images/')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, db_index=True)  # Adding index on category

    def __str__(self):
        return self.name
