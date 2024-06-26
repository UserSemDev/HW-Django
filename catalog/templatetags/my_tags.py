from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(needs_autoescape=True)
def replace_newline(value, autoescape=True):
    if autoescape:
        if '\r\n' in value:
            result = value.replace('\r\n', '<br/>')
            return mark_safe(result)
        return value


@register.filter
def media_url(data):
    if data:
        return f"/media/{data}"
    return "#"


@register.filter
def season_name(data):
    if data:
        season = {
            'WNR': 'Зима',
            'SRG': 'Весна',
            'SMR': 'Лето',
            'ATN': 'Осень'}
        return f"{season.get(data)}"
    return "Bug"
