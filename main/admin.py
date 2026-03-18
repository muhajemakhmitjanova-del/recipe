from django.contrib import admin
from .models import *


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
     pass

    

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    pass
   

@admin.register(When)
class WhenAdmin(admin.ModelAdmin):
    pass

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass
  