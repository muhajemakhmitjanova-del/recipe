from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'country', 'food', 'when', 'recipe_text', 'image']

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Название рецепта',
                'class': 'form-input'
            }),

            'country': forms.Select(attrs={
                'class': 'form-select'
            }),

            'food': forms.Select(attrs={
                'class': 'form-select'
            }),

            'when': forms.SelectMultiple(attrs={
                'class': 'form-select',
                'size': 5
            }),

            'recipe_text': forms.Textarea(attrs={
                'placeholder': 'Описание рецепта',
                'class': 'form-textarea',
                'rows': 5
            }),

            'image': forms.ClearableFileInput(attrs={
                'class': 'form-file'
            }),
        }

        labels = {
            'name': 'Название',
            'country': 'Страна',
            'food': 'Тип блюда',
            'when': 'Когда готовить',
            'recipe_text': 'Рецепт',
            'image': 'Картинка',
        }