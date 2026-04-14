from django.shortcuts import render
from main.models import *
from api.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    
class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer



class FoodList(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    
class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    
    
    
class WhenList(generics.ListCreateAPIView):
    queryset = When.objects.all()
    serializer_class = WhenSerializer
    
class WhenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = When.objects.all()
    serializer_class = WhenSerializer
    
    
    
class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    
    
class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    
    
     
# @api_view(['GET',"POST"])
# def recipe_views(request):
#     if request.method == "GET":
#         recipe_list = Recipe.objects.all()
#         serializer = RecipeSerializer(recipe_list,many= True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = RecipeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status = 201)
        
        
# @api_view(['GET','PUT','DELETE'])
# def recipe_detail(request, pk):
#     try:
#         recipe = Recipe.objects.get(id=pk)
#     except Recipe.DoesNotExist:
#         return Response(status=404)

#     if request.method == "GET":
#         serializer = RecipeSerializer(recipe)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = RecipeSerializer(recipe, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#     elif request.method == "DELETE":
#         recipe.delete()
#         return Response(status=204)
   
   
    
# @api_view(['GET','POST'])
# def country_views(request):
#     if request.method == "GET":
#         country_list = Country.objects.all()
#         serializer = CountrySerializer(country_list,many= True)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = CountrySerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status = 201)
        
        
        
# @api_view(['GET','PUT','DELETE'])
# def country_detail(request, pk):
#     try:
#         country = Country.objects.get(id=pk)
#     except Country.DoesNotExist:
#         return Response(status=404)

#     if request.method == "GET":
#         serializer = CountrySerializer(country)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = CountrySerializer(country, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#     elif request.method == "DELETE":
#         country.delete()
#         return Response(status=204)
    

# @api_view(['GET','POST'])
# def food_views(request):
#     if request.method == "GET":
#         food_list = Food.objects.all()
#         serializer = FoodSerializer(food_list,many= True)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = FoodSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status = 201)
        
        
# @api_view(['GET','PUT','DELETE'])
# def food_detail(request, pk):
#     try:
#         food = Food.objects.get(id=pk)
#     except Food.DoesNotExist:
#         return Response(status=404)

#     if request.method == "GET":
#         serializer = FoodSerializer(food)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = FoodSerializer(food, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#     elif request.method == "DELETE":
#         food.delete()
#         return Response(status=204)
    
    
# @api_view(['GET','POST'])
# def when_views(request):
#     if request.method == "GET":
#         when_list = When.objects.all()
#         serializer = WhenSerializer(when_list,many= True)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = WhenSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status = 201)
        
        
# @api_view(['GET','PUT','DELETE'])
# def when_detail(request, pk):
#     try:
#         when = When.objects.get(id=pk)
#     except When.DoesNotExist:
#         return Response(status=404)

#     if request.method == "GET":
#         serializer = WhenSerializer(when)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = WhenSerializer(when, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#     elif request.method == "DELETE":
#         when.delete()
#         return Response(status=204)