from django.urls import path
from .views import *

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/<int:pk>/edit/', RecipeUpdateView.as_view(), name='change_recipe'),
    path('recipe/<int:pk>/delete/', RecipeDeleteView.as_view(), name='delete_recipe'),
    path('type/<int:food_id>/', RecipesByTypeView.as_view(), name='recipes_by_type'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('country_detail/<int:country_id>/', CountryDetailView.as_view(), name='country_detail'),
    path('when_detail/<int:when_id>/', WhenDetailView.as_view(), name='when_detail'),
]