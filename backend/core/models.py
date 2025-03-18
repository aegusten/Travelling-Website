from django.db import models
from django.contrib.auth.models import AbstractUser

class Country(models.Model):
    VISA_CHOICES = [
        ('No Visa Required', 'No Visa Required'),
        ('E-Visa Available', 'E-Visa Available'),
        ('Visa Required', 'Visa Required'),
    ]

    country_name = models.CharField(max_length=100, unique=True)        
    country_code = models.CharField(max_length=100, blank=True)   
    currency_code = models.CharField(max_length=100, blank=True) 
    currency_name = models.CharField(max_length=100, blank=True)
    
    visa_requirement = models.CharField(
        max_length=50, choices=VISA_CHOICES, blank=True
    )
    
    average_travel_cost = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    
    description = models.TextField(blank=True)
    image_url = models.TextField(blank=True)

    def __str__(self):
        return self.country_name


class CustomUser(AbstractUser):
    country = models.ForeignKey(
        Country, null=True, blank=True, on_delete=models.SET_NULL
    )
    
    budget = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    
    currency = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.username
