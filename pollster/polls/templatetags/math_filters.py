from django import template

register = template.Library()

@register.filter
def floatdiv(value, divisor):
    try:
        return float(value) / float(divisor)
    except (ValueError, ZeroDivisionError):
        return 0

@register.filter
def mul(value, arg):
    try:
        return float(value) * float(arg)
    except ValueError:
        return 0
