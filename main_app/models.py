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
