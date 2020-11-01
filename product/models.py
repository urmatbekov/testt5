from django.db import models


# Create your models here.
class Product(models.Model):
    image = models.ImageField(upload_to='image')
    title = models.CharField(max_length=120)
    category = models.CharField(max_length=120)
    price = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title
