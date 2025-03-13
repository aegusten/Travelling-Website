from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser
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

class VisaRule(models.Model):
    VISA_CHOICES = [
        ('No Visa Required', 'No Visa Required'),
        ('E-Visa Available', 'E-Visa Available'),
        ('Visa Required', 'Visa Required'),
    ]
    country = models.ForeignKey(Country, related_name='visa_rules', on_delete=models.CASCADE)
    passport_country = models.ForeignKey(Country, related_name='passport_rules', on_delete=models.CASCADE)
    visa_requirement = models.CharField(max_length=50, choices=VISA_CHOICES)
    visa_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    processing_time_days = models.IntegerField(null=True, blank=True)
    additional_requirements = models.TextField(blank=True)
    max_stay_days = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.passport_country.name} -> {self.country.name} ({self.visa_requirement})"
