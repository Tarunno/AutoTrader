from django.contrib import admin
from .models import Customer

admin.site.site_header = 'AutoTrader | admin'

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'image', 'location']
