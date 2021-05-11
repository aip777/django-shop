from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.category_name

class Products(models.Model):
    name = models.CharField(max_length=100, blank=False)
    code = models.IntegerField(blank=False)
    category =  models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField(blank=False, max_length=10)
    current_stock = models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        obj = self.name
        return obj