from django.db import models


# Create your models here.


class ProdFood(models.Model):
    prod_code = models.CharField(max_length=20)
    prod_name = models.CharField(max_length=200)
    prod_price = models.FloatField()
    prod_image = models.ImageField(default='kkkk')
    prod_gallery = models.CharField(max_length=200)

    class Meta:
        ordering = ('prod_code',)
