from django import template

register = template.Library()


@register.filter
def is_moderator(user):
    return user.groups.filter(name='Moderator').exists()


@register.filter
def is_content_manager(user):
    return user.groups.filter(name='Content manager').exists()
