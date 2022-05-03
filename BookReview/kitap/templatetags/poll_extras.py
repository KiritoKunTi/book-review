from atexit import register
from django import template
from kitap.models import *
register = template.Library()

@register.simple_tag(name='getfaqs')
def get_faqs():
    return Faq.objects.all()

@register.simple_tag(name='getcats')
def get_categories():
    return Category.objects.all()
        