from django  import template

register=template.Library()

@register.filter(name='gettotal')

def gettotal(cart):
    total=0
    for item in cart.added_items.all():
        price=item.product.orginal_price()
        total=total+item.quantity*price
    return total