from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login as auth_login
from .models import *
from .form import *
from django.views import View


class MainPageView(ListView):
    model = Recipe
    template_name = 'index.html'
    context_object_name = 'recipes'
    
    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(name__icontains=query)
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countries'] = Country.objects.all()
        context['foods'] = Food.objects.all()
        context['whens'] = When.objects.all()
        return context


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countries'] = Country.objects.all()
        context['foods'] = Food.objects.all()
        context['whens'] = When.objects.all()
        context['recipes'] = Recipe.objects.all()
        return context

class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'create_recipe.html'
    
    def get_success_url(self):
        return reverse_lazy('recipe_detail', kwargs={'pk': self.object.pk})


class RecipeUpdateView(UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'change_recipe.html'
    
    def get_success_url(self):
        return reverse_lazy('recipe_detail', kwargs={'pk': self.object.pk})


class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'delete_recipe.html'
    success_url = reverse_lazy('main_page')
    

class RecipesByTypeView(ListView):
    model = Recipe
    template_name = 'recipes_by_type.html'
    context_object_name = 'recipes'
    
    def get_queryset(self):
        food_id = self.kwargs['food_id']
        return Recipe.objects.filter(food__id=food_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['foods'] = Food.objects.all()
        context['countries'] = Country.objects.all()
        context['whens'] = When.objects.all()
        return context

class CountryDetailView(ListView):
    model = Recipe
    template_name = 'country_detail.html'
    context_object_name = 'recipes'
    
    def get_queryset(self):
        country_id = self.kwargs['country_id']
        return Recipe.objects.filter(country__id=country_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['foods'] = Food.objects.all()
        context['countries'] = Country.objects.all()
        context['whens'] = When.objects.all()
        return context
    
    
class WhenDetailView(ListView):
    model = Recipe
    template_name = 'when_detail.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        when_id = self.kwargs['when_id']
        return Recipe.objects.filter(when__id=when_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selected_when'] = get_object_or_404(When, id=self.kwargs['when_id'])
        context['countries'] = Country.objects.all()
        context['foods'] = Food.objects.all()
        context['whens'] = When.objects.all()
        return context
    
    
class CustomLoginView(LoginView):
    template_name = 'login.html'
    
    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return redirect('main_page')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')
    
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('password2')
        
        if password != confirm_password:
            messages.error(request, 'Пароли не совпадают.')
            return render(request, 'register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Пользователь с таким именем уже существует.')
            return render(request, 'register.html')
        
        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, 'Регистрация прошла успешно. Теперь вы можете войти.')
        return redirect('login')



    
    
    