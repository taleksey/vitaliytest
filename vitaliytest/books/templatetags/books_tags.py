from django import template
from django.core import urlresolvers

register = template.Library()

@register.simple_tag
def edit_link(edit_object):
    try:
        id =  edit_object.id
        change_url = urlresolvers.reverse('admin:%s_%s_change' %(edit_object._meta.app_label,  edit_object._meta.module_name), args=(id,))
    except AttributeError:
        raise template.TemplateSyntaxError("Tag requires correct Object")
    return change_url


