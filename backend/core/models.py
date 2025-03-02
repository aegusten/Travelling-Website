from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    passport_country = models.ForeignKey('Country', null=True, blank=True, on_delete=models.SET_NULL)
    preferred_travel_style = models.CharField(max_length=50, blank=True)
    dietary_needs = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username

class Country(models.Model):
    VISA_CHOICES = [
        ('No Visa Required', 'No Visa Required'),
        ('E-Visa Available', 'E-Visa Available'),
        ('Visa Required', 'Visa Required'),
    ]
    name = models.CharField(max_length=100, unique=True)
    visa_requirement = models.CharField(max_length=50, choices=VISA_CHOICES)
    average_travel_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    currency = models.CharField(max_length=10, blank=True)
    language = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class VisaRule(models.Model):
    country = models.ForeignKey(Country, related_name='visa_rules', on_delete=models.CASCADE)
    passport_country = models.ForeignKey(Country, related_name='passport_rules', on_delete=models.CASCADE)
    visa_requirement = models.CharField(max_length=50, choices=Country.VISA_CHOICES)

    def __str__(self):
        return f"{self.passport_country} -> {self.country} : {self.visa_requirement}"

class BudgetRecommendation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    recommended_budget = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.username}: {self.country.name} (${self.recommended_budget})"
