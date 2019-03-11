from django import template

register = template.Library()

@register.filter(name='following_user')
def following_user(value,arg):
    from_user = value
    search_user = arg
    return from_user.following.all().filter(user=search_user).exists()
