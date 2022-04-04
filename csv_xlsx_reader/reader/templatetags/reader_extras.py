from django import template

register = template.Library()


@register.filter
def show_index(value, args):
    return list(args).index(value) + 1
