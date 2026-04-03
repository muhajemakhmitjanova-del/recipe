from main.models import *
from rest_framework import serializers

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

class WhenSerializer(serializers.ModelSerializer):
    class Meta:
        model = When
        fields = '__all__'
