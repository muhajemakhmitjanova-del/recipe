import os 
from django.db.models.signals import *
from django.dispatch import receiver

from .models import Recipe

@receiver(post_delete,sender=Recipe )
def delete_recipe(sender,instance,**kwargs):
    if instance.image:
        if os.path.isfile(instance.path):
            os.remove(instance.image.path)
            
      
        
@receiver(post_save, sender = Recipe)
def create_recipe(sender, instance, created, **kwargs):
    if created:
        print(f"Создан фильм {instance.name}")
    else:
        print(f"Обновлен фильм {instance.name}")
        
        
        
@receiver(pre_save, sender = Recipe)
def raiting_update(sender,instance,**kwargs):
    if instance.raiting > 5:
        instance.raiting = 5
        
    elif instance.raiting < 5:
        instance.raiting = 5
        
    
        