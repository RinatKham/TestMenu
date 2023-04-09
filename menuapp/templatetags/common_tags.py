from django import template
from menuapp.models import MenuItem
register = template.Library()


@register.inclusion_tag('templatetags/menu.html', takes_context=False)
def show_menu():
    menu_items = MenuItem.objects.all
    return {
        "menu_items": menu_items,
    }
