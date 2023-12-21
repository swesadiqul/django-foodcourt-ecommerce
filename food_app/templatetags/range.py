from django import template

register = template.Library()


@register.filter
def filter_range(start, end):
    return range(start, end)