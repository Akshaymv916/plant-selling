from django  import template

register=template.Library()

@register.filter(name='total')

def total(cart):
    total=0
    for item in cart.added_items.all():
        price=item.product.orginal_price()
        total=total+item.quantity*price
        total=int(total)
    total=total+35
    return total