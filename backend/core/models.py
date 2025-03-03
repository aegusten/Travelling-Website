from django.db import models
from django.contrib.auth.models import AbstractUser

# 1. Country Model
class Country(models.Model):
    VISA_CHOICES = [
        ('No Visa Required', 'No Visa Required'),
        ('E-Visa Available', 'E-Visa Available'),
        ('Visa Required', 'Visa Required'),
    ]
    visa_requirement = models.CharField(max_length=50, choices=VISA_CHOICES, blank=True)

    name = models.CharField(max_length=100, unique=True)
    average_travel_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    currency = models.CharField(max_length=10, blank=True)
    language = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    image_url = models.TextField(blank=True)

    def __str__(self):
        return self.name


# 2. Custom User Model
class CustomUser(AbstractUser):
    
    passport_country = models.ForeignKey(
        Country, null=True, blank=True, on_delete=models.SET_NULL
    )

    preferred_travel_style = models.CharField(max_length=50, blank=True)
    dietary_needs = models.CharField(max_length=100, blank=True)
    travel_group_size = models.IntegerField(null=True, blank=True)
    accessibility_needs = models.TextField(blank=True)

    def __str__(self):
        return self.username


# 3. User Preferences (Consolidated)
class UserPreferences(models.Model):
    TRANSPORT_MODE_CHOICES = [
        ('Train', 'Train'),
        ('Bus', 'Bus'),
        ('Car Rental', 'Car Rental'),
        ('Other', 'Other'),
    ]
    CLASS_CHOICES = [
        ('Economy', 'Economy'),
        ('Business', 'Business'),
        ('First Class', 'First Class'),
    ]
    ACCOMMODATION_TYPE_CHOICES = [
        ('Hotel', 'Hotel'),
        ('Hostel', 'Hostel'),
        ('Vacation Rental', 'Vacation Rental'),
        ('Other', 'Other'),
    ]
    ACTIVITY_CATEGORY_CHOICES = [
        ('Sightseeing', 'Sightseeing'),
        ('Adventure', 'Adventure'),
        ('Relaxation', 'Relaxation'),
        ('Cultural', 'Cultural'),
        ('Other', 'Other'),
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    # Budget fields
    accommodation_budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    transportation_budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    food_budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    activities_budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    miscellaneous_budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # Accommodation
    accommodation_type = models.CharField(
        max_length=50,
        choices=ACCOMMODATION_TYPE_CHOICES,
        blank=True
    )
    preferred_location = models.CharField(max_length=255, blank=True)
    required_amenities = models.TextField(blank=True)

    # Transportation (No "Flight")
    transportation_mode = models.CharField(
        max_length=50,
        choices=TRANSPORT_MODE_CHOICES,
        blank=True
    )
    class_preference = models.CharField(
        max_length=50,
        choices=CLASS_CHOICES,
        blank=True
    )
    rental_car_type = models.CharField(max_length=50, blank=True)

    # Activities
    activity_category = models.CharField(
        max_length=100,
        choices=ACTIVITY_CATEGORY_CHOICES,
        blank=True
    )
    specific_interests = models.TextField(blank=True)

    # Dining
    cuisine_preferences = models.TextField(blank=True)
    dining_budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Preferences for {self.user.username}"


# 4. Visa Rules (One Table, More Detailed)
class VisaRule(models.Model):
    VISA_CHOICES = [
        ('No Visa Required', 'No Visa Required'),
        ('E-Visa Available', 'E-Visa Available'),
        ('Visa Required', 'Visa Required'),
    ]

    country = models.ForeignKey(
        Country, related_name='visa_rules', on_delete=models.CASCADE
    )
    passport_country = models.ForeignKey(
        Country, related_name='passport_rules', on_delete=models.CASCADE
    )
    visa_requirement = models.CharField(max_length=50, choices=VISA_CHOICES)

    # Optional fields
    visa_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    processing_time_days = models.IntegerField(null=True, blank=True)
    additional_requirements = models.TextField(blank=True)

    def __str__(self):
        return f"{self.passport_country.name} -> {self.country.name} ({self.visa_requirement})"


# 5. Budget Recommendation (Optional AI or custom logic)
class BudgetRecommendation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    recommended_budget = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.username}: {self.country.name} (${self.recommended_budget})"


# 6. Points of Interest (Activities, Events, Accommodations in One)
class PointOfInterest(models.Model):
    CATEGORY_CHOICES = [
        ('Activity', 'Activity'),
        ('Event', 'Event'),
        ('Accommodation', 'Accommodation'),
        ('Restaurant', 'Restaurant'),
        ('Transportation', 'Transportation'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    average_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    image_url = models.TextField(blank=True)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='Activity'
    )

    # Optional fields for events
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.category})"


# 7. POI Recommendations
class POIRecommendation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    poi = models.ForeignKey(PointOfInterest, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} -> {self.poi.name} ({self.score})"


# 8. Itinerary + Itinerary Items
class Itinerary(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    total_budget = models.DecimalField(max_digits=10, decimal_places=2)


    destination_country = models.ForeignKey(
        Country, null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return f"{self.user.username} - {self.name}"


class ItineraryItem(models.Model):
    CATEGORY_CHOICES = [
        ('Accommodation', 'Accommodation'),
        ('Transportation', 'Transportation'),
        ('Activity', 'Activity'),
        ('Meal', 'Meal'),
        ('Other', 'Other'),
    ]

    itinerary = models.ForeignKey(
        Itinerary, on_delete=models.CASCADE, related_name='items'
    )
    date = models.DateField()
    location = models.CharField(max_length=255, blank=True)
    activity = models.CharField(max_length=255, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='Other'
    )

    def __str__(self):
        return f"{self.itinerary.name} - {self.activity} on {self.date}"


# 9. Reviews (on Countries)
class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.country.name}: {self.rating}"


# 10. Bookings
class Booking(models.Model):
    STATUS_CHOICES = [
        ('Booked', 'Booked'),
        ('Pending', 'Pending'),
        ('Cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.itinerary.name} ({self.status})"
