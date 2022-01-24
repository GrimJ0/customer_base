import ast

from django import template

register = template.Library()


@register.filter
def addcss(field, attrs):
    """Функция добавляет class к полю"""
    attrs = ast.literal_eval(attrs)
    return field.as_widget(attrs=attrs)
