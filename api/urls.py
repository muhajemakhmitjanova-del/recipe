from .views import *
from django.urls import path,include

urlpatterns = [
    path('recipes/', recipe_views),
    path('recipes/<int:pk>/', recipe_detail),
    path('countries/', country_views),
    path('countries/<int:pk>/', country_detail),
    path('foods/', food_views),
    path('foods/<int:pk>/', food_detail),
    path('whens/', when_views),
    path('whens/<int:pk>/', when_detail),
]