from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="customer/default.jpg", upload_to="customer/", null=True, blank=True)
    phone = models.CharField(max_length=256, null=True, blank=True)
    location = models.CharField(max_length=256, null=True, blank=True)

    auction_posted = models.IntegerField(default=0)

    def __str__(self):
         return self.user.username

    def save(self, *args, **kwargs):
        super(Customer, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.image.path)

            