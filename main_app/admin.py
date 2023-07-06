from django.contrib import admin
from .models import Recipe, Ingredients, ShoppingLists

admin.site.register(Recipe)
admin.site.register(Ingredients)
admin.site.register(ShoppingLists)

# Register your models here.
