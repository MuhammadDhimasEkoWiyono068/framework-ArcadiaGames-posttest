from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Games(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    developer = models.CharField(max_length=255)
    release_date = models.DateField()

    def __str__(self):
        return self.title
