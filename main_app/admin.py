from django.contrib import admin
from .models import Recipe, Ingredients, Shopping_Lists

admin.site.register(Recipe)
admin.site.register(Ingredients)
admin.site.register(Shopping_Lists)

# Register your models here.
