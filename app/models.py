from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone

class Car(models.Model):
    MAKE = [('BMW', 'BMW'),
            ('Toyota', 'Toyota'),
            ('Ford', 'Ford'),
            ('Honda', 'Honda'),
            ('Jeep', 'Jeep'),
            ('Mercedes', 'Mercedes')]
    BODY_STYLE = [('Coupe', 'Coupe'),
                  ('Convertible', 'Convertible'),
                  ('Sedan', 'Sedan'),
                  ('Hatchback', 'Hatchback'),
                  ('SUV/CUV', 'SUV/CUV'),
                  ('Truck', 'Truck'),
                  ('Van/Minivan', 'Van/Minivan'),
                  ('Wagon', 'Wagon')]
    DRIVETRAIN = [('Rear-wheel', 'Rear-wheel'),
                  ('Front-wheel', 'Front-wheel'),
                  ('All-wheel', 'All-wheel')]
    TRANSMISSION = [('Automatic', 'Automatic'),
                    ('Manual', 'Manual'),
                    ('Automatic-Menual', 'Automatic with Menual')]
    TRANSMISSION_SPEED = [(i, i) for i in range(1, 10)]
    SELLER_TYPE = [('Dealer', 'Dealer'),
                   ('Customer', 'Customer')]

    make = models.CharField(max_length=100, null=True, blank=True, choices=MAKE)
    model = models.CharField(max_length=100, null=True, blank=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    vin = models.CharField(max_length=200, null=True, blank=True)
    mileage = models.CharField(max_length=200, null=True, blank=True)
    body_style = models.CharField(max_length=100, null=True, blank=True, choices=BODY_STYLE)
    engine = models.CharField(max_length=100, null=True, blank=True)
    drivetrain = models.CharField(max_length=100, null=True, blank=True, choices=DRIVETRAIN)
    transmission = models.CharField(max_length=100, null=True, blank=True, choices=TRANSMISSION)
    transmission_speed = models.IntegerField(null=True, blank=True, choices=TRANSMISSION_SPEED)
    exterior_color = models.CharField(max_length=100, null=True, blank=True)
    interior_color = models.CharField(max_length=100, null=True, blank=True)
    title_status = models.CharField(max_length=100, null=True, blank=True)
    seller_type = models.CharField(max_length=100, null=True, blank=True, choices=SELLER_TYPE)
    highlight = models.TextField(null=True, blank=True)
    equipment = models.TextField(null=True, blank=True)
    modification = models.TextField(null=True, blank=True)
    known_flaw = models.TextField(null=True, blank=True)
    recent_service_history = models.TextField(null=True, blank=True)
    ownership_history = models.TextField(null=True, blank=True)
    seller_note = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    end_at = models.DateTimeField(default=timezone.now, null=True, blank=True)
    bid = models.IntegerField(default=1000, null=True, blank=True)
    on_auction = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        return self.make + ' ' + self.model


class Photo(models.Model):
    TYPE = [('Interior', 'Interior'),
            ('Exterior', 'Exterior')]
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='car/', null=False, blank=False)
    type = models.CharField(max_length=100, null=False, blank=False, choices=TYPE)

    def save(self, *args, **kwargs):
        super(Photo, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 1000 or img.width > 1000:
            output_size = (1000, 1000)
            img.thumbnail(output_size)
            img.save(self.image.path)

