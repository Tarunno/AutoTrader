from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone

class Car(models.Model):
    MAKE = [('BMW', 'BMW'),
            ('Toyota', 'Toyota'),
            ('Ford', 'Ford'),
            ('Honda', 'Honda')]
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

    make = models.CharField(max_length=100, null=False, blank=False, choices=MAKE)
    model = models.CharField(max_length=100, null=False, blank=False)
    seller = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    location = models.CharField(max_length=200, null=False, blank=False)
    vin = models.CharField(max_length=200, null=False, blank=False)
    mileage = models.CharField(max_length=200, null=False, blank=False)
    body_style = models.CharField(max_length=100, null=False, blank=False, choices=BODY_STYLE)
    engine = models.CharField(max_length=100, null=False, blank=False)
    drivetrain = models.CharField(max_length=100, null=False, blank=False, choices=DRIVETRAIN)
    transmission = models.CharField(max_length=100, null=False, blank=False, choices=TRANSMISSION)
    transmission_speed = models.IntegerField(choices=TRANSMISSION_SPEED)
    exterior_color = models.CharField(max_length=100, null=False, blank=False)
    interior_color = models.CharField(max_length=100, null=False, blank=False)
    title_status = models.CharField(max_length=100, null=False, blank=False)
    seller_type = models.CharField(max_length=100, null=False, blank=False, choices=SELLER_TYPE)
    highlight = models.TextField(null=False, blank=False)
    equipment = models.TextField(null=False, blank=False)
    modification = models.TextField(null=False, blank=False)
    known_flaw = models.TextField(null=False, blank=False)
    recent_service_history = models.TextField(null=False, blank=False)
    ownership_history = models.TextField(null=False, blank=False)
    seller_note = models.CharField(max_length=300, null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    end_at = models.DateTimeField(default=timezone.now, null=False, blank=True)

    def __str__(self):
        return self.make + ' ' + self.model


class Photo(models.Model):
    TYPE = [('Interior', 'Interior'),
            ('Exterior', 'Exterior')]
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car/', null=False, blank=False)
    type = models.CharField(max_length=100, null=False, blank=False, choices=TYPE)

    def save(self, *args, **kwargs):
        super(Photo, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 1000 or img.width > 1000:
            output_size = (1000, 1000)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return self.car.make + ' ' + self.car.make + ' ' + self.car.image
