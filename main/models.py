from django.db import models


class Country(models.Model):
    name = models.CharField(verbose_name='Страна', max_length=50, unique=True)
    slug = models.SlugField(verbose_name='Слаг', max_length=50, unique=True)

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(verbose_name='Тип', max_length=50)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self):
        return self.name


class When(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Когда готовить"
        verbose_name_plural = "Когда готовить"

    def __str__(self):
        return self.name


class Recipe(models.Model):
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='recipes'
    )

    food = models.ForeignKey(
        Food,
        on_delete=models.CASCADE,
        related_name='recipes'
    )

    when = models.ManyToManyField(
    When,
    blank=True,
    related_name='recipes'
)

    name = models.CharField(
        verbose_name='Название',
        max_length=250
    )

    recipe_text = models.TextField(
        verbose_name='Рецепт'
    )

    image = models.ImageField(
        verbose_name="Картинка",
        upload_to='recipes/images/',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name