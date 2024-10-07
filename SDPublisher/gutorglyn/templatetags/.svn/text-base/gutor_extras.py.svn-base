from django import template

register = template.Library()

@register.filter
def trimRef(value):
    '''Trim full stop and all trailing characters from value'''
    seperator = '.'
    return value.split(seperator, 1)[0]