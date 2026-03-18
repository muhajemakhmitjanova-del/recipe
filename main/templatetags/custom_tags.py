from django import template

from main.models import *

register = template.Library()

@register.simple_tag
def get_when():
    return When.objects.all()
