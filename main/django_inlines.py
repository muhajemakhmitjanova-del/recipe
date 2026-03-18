from django.contrib import admin
from .models import Recipe, Food, When


class RecipeInline(admin.TabularInline):
    model = Recipe
    extra = 1


class FoodInline(admin.TabularInline):
    model = Food
    extra = 1


class WhenInline(admin.TabularInline):
    model = When
    extra = 1