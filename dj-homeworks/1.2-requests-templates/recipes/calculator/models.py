from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.quantity}"


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.title

