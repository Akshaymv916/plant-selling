from django  import template

register=template.Library()

@register.filter(name='getstatus')

def getstatus(status):
    status=status-1
    status_array=['confiremed','processed','delivered','rejected']
    return status_array[status]