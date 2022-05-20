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

@register.filter(name='times') 
def times(number):
    return range(1,number)

@register.filter()
def to_int(value):
    return int(value)        
        