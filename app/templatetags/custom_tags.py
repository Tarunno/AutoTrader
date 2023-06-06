from django import template

register = template.Library()

@register.filter
def split(value):
    lines = value.split("-")
    return lines[1:]

@register.filter
def sum_number(val1, val2):
    return int(val1) + int(val2)