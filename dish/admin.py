from django.contrib import admin
from .models import Dish
# Register your models here.

class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ['name'] 
    fields = ('name', 'price', 'calories')
    # readonly_fields = ['name']

admin.site.register(Dish, DishAdmin)