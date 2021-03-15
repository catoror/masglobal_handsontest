from django import template
import datetime as dt

register = template.Library()

@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class":css})
   
@register.filter(name='hace_horas')
def hours_ago(time, hours):
    print(time)
    print(time + dt.timedelta(hours=hours))
    print(dt.datetime.now())
    print(time + dt.timedelta(hours=hours) < dt.datetime.now())
    print()
    
    return time + dt.timedelta(hours=hours) < dt.datetime.now() # or timezone.now() if your time is offset-aware

@register.filter(name='reemplaza_coma_por_punto')
def replace_comma_by_dot(value):
    return str(value).replace(",",".")

@register.filter(name='split')
def split(value, key):
    """
        Returns the value turned into a list.
    """
    return value.split(key)

@register.filter(name='to_string')
def to_string(value):
    """
        Returns the value turned into a list.
    """
    return str(value)