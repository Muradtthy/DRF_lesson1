from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('Category Name', max_length=50)

    def __str__(self):
        return self.name
    
class Car(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='car_category')
    name = models.CharField('Car Name', max_length=50)
    price = models.PositiveIntegerField('Car Price')


    def __str__(self):
        return self.name