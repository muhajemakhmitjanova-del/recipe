from django import template

register = template.Library()

@register.filter
def excited(value):
    return f"{value}!!!"

@register.filter
def lower_list(value):
    return value.lower()


@register.filter
def capitalize_list(value):
    return value.capitalize()