from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    instructions = models.TextField(max_length=2000)
    link = models.CharField(max_length=250)

    def __str__(self):
        return "Recipe: " + self.name
    class Meta:
        ordering = ['name']

class Ingredients(models.Model):
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=150)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")

    def __str__(self):
        return self.name
    
class Shopping_Lists(models.Model):
    list_name = models.CharField(max_length=150)
    ingredients = models.ManyToManyField(Ingredients)

    def __str__(self):
        return self.list_name
    class Meta:
        ordering = ['list_name']