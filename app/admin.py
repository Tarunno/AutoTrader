from django.contrib import admin
from .models import Car, Photo

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['make', 'model',  'body_style', 'engine', 'transmission']
    list_filter = ['make', 'body_style', 'transmission']

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['make', 'model', 'image']
    list_filter = ['car__make']
    def make(self, obj):
        return obj.car.make

    def model(self, obj):
        return obj.car.model
