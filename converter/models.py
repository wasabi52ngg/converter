from django.db import models
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
class Currency(models.Model):

    EUR = 'EUR'
    USD = 'USD'
    RUB = 'RUB'
    Currency_choices = [
        (EUR, 'Euro'),
        (USD, 'Dollars'),
        (RUB, 'Rubles'),
    ]

    name = models.CharField(max_length=3, choices=Currency_choices)
    value_in_USD = models.FloatField()

    def __str__(self):
        return f'{self.name}'
