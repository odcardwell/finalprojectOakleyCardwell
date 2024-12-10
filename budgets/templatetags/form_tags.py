# INF601 - Advanced Programming in Python
# Oakley Cardwell
# Final Project

# This file is used for custom template tags in the budgets template form.
from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})
