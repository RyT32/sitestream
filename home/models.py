from django.db import models

# Create your models here.
class Card(models.Model):
    name = models.TextField(
        max_length=255, 
        verbose_name="Наименование")
    price = models.DecimalField(
        verbose_name="Цена"
    )
    