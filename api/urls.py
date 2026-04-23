from .views import *
from django.urls import path, include

urlpatterns = [
    path('', include('api.yasg')),
    path("auth/", include("api.auth.urls")),

    path('recipes/', RecipeList.as_view()),
    path('recipes/<int:pk>/', RecipeDetail.as_view()),

    path('countries/', CountryList.as_view()),
    path('countries/<int:pk>/', CountryDetail.as_view()),

    path('foods/', FoodList.as_view()),
    path('foods/<int:pk>/', FoodDetail.as_view()),

    path('whens/', WhenList.as_view()),
    path('whens/<int:pk>/', WhenDetail.as_view()),
]