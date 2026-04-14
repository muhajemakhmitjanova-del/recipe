from django.contrib import admin
from .models import *
from django.utils.html import format_html

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug',)
    search_fields = ('name','id',)
    
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    search_fields = ('name','id',)


@admin.register(When)
class WhenAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    search_fields = ('name','id',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'food', 'when', 'image_tag', )
    search_fields = ('name','id','food__name','when__name',)
    def image_tag(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="70" height="70" style="object-fit:cover;" />',
                obj.image.url
            )
        return "—"

    image_tag.short_description = "Image"