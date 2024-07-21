from django.conf import settings
from django.shortcuts import redirect, render
from home.decorator import session_handler
from home.models import Customuser
from django.contrib import messages

from product.models import Products
from userprofile.models import Address
from django.views.decorators.csrf import csrf_exempt

from .models import  Cancelorder, Checkout, Order, Orderitem, Payment, Wishlist
import razorpay
client=razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRATE))


@session_handler
def addcart(request,id,username=None):
    if username:
        if request.method=='POST':
            quantity=int(request.POST['quan'])

            pro=Products.objects.get(id=id)
            allpro=Products.objects.all()
            cart_obj,created=Order.objects.get_or_create(
                owner=username,
                order_status=Order.CART_STAGE
            )
        if pro.quantity>=quantity:
            pro.quantity-=quantity
            pro.save()
            if pro.quantity>=quantity:
                  pro.stock=Products.OUT_OF_STOCK
                  pro.save()
            orderitem,created=Orderitem.objects.get_or_create(
                product=pro,
                owner=cart_obj,
                item_status=Order.CART_STAGE
                
            )
            if created:
                orderitem.quantity=quantity
                orderitem.save()
                messages.success(request,f"{pro} add to cart",)
                return redirect(request.META.get('HTTP_REFERER'))
            else:
                orderitem.quantity=orderitem.quantity+quantity
                orderitem.save()
            messages.success(request,f"{pro} add to cart",)
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            pro.stock=Products.OUT_OF_STOCK
            pro.save()
            messages.info(request,'Out of stock ')
            return redirect(request.META.get('HTTP_REFERER'))

    return redirect('login')


@session_handler
def quickaddcart(request,id,username=None):
    if username:
        pro=Products.objects.get(id=id)
        cart_obj,created=Order.objects.get_or_create(
            owner=username,
            order_status=Order.CART_STAGE
        )

        if pro.quantity>=1:
            pro.quantity-=1
            pro.save()
            if pro.quantity<1:
                  pro.stock=Products.OUT_OF_STOCK
                  pro.save()
            orderitem,created=Orderitem.objects.get_or_create(
                product=pro,
                owner=cart_obj,
                item_status=Order.CART_STAGE
                
            )
            if created:
                orderitem.quantity=1
                orderitem.save()
                messages.success(request,f"{pro} added to cart",)
                return redirect(request.META.get('HTTP_REFERER'))
            else:
                orderitem.quantity=orderitem.quantity+1
                orderitem.save()
                messages.success(request,f"{pro} added to cart")
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.info(request,'Out of stock ')
            return redirect(request.META.get('HTTP_REFERER'))
    return redirect('login')


@session_handler
def quickaddwish(request,id,username=None):
    if username:
        pro=Products.objects.get(id=id)
        cart_obj,created=Order.objects.get_or_create(
            owner=username,
            order_status=Order.CART_STAGE
        )

        if pro.quantity>=1:
            pro.quantity-=1
            pro.save()
            if pro.quantity<1:
                  pro.stock=Products.OUT_OF_STOCK
                  pro.save()
            orderitem,created=Orderitem.objects.get_or_create(
                product=pro,
                owner=cart_obj,
                
            )
            if created:
                orderitem.quantity=1
                orderitem.save()
            else:
                orderitem.quantity=orderitem.quantity+1
                orderitem.save()
                wish=Wishlist.objects.get(product_id=pro)
                print(pro)
                wish.delete()
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.info(request,'Out of stock ')
            return redirect(request.META.get('HTTP_REFERER'))
    return redirect('login')

def removeitem(request,id):
    orderitem=Orderitem.objects.get(id=id)
    pro=Products.objects.get(added_carts=orderitem)
    print(pro)
    pro.quantity=pro.quantity+orderitem.quantity
    pro.save()
    orderitem.delete()
    messages.success(request,f"{pro} removed",)
    return redirect(request.META.get('HTTP_REFERER'))


@session_handler
def add_to_wish(request,id,username=None):
     if username:
          product=Products.objects.get(id=id)
          if not Wishlist.objects.filter(product_id=product,user_id=username):
               wish=Wishlist.objects.create(product_id=product,user_id=username)
               messages.success(request,f"{product} added",)
               wish.save()
               return redirect(request.META.get('HTTP_REFERER'))
          else:
               messages.info(request,'already added to wishlist')
               return redirect(request.META.get('HTTP_REFERER'))
     messages.info(request,'Please login')
     return redirect('login')

@session_handler
def removewish(request,id,username=None):
     if username:
          p=Products.objects.get(id=id)
          product=Wishlist.objects.get(product_id=id)
          product.delete()
          messages.success(request,f"{p} removed",)
          return redirect(request.META.get('HTTP_REFERER'))
     messages.info(request,'Please login')
     return redirect('login')


def checkwishlist(user,product_id):
     in_wish=Wishlist.objects.filter(user_id=user,product_id=product_id).exists()
     return in_wish


@session_handler
def wishlist(request,username=None):
     if username:
            product=Wishlist.objects.all()
            cart_obj,created=Order.objects.get_or_create(
                owner=username,
                order_status=Order.CART_STAGE
            )
            wish=Wishlist.objects.all()
            context=   {
                'product':product,
                'cart':cart_obj,
                'username':username,
                'wish':wish
            }
            return render(request,'userprofile/wishlist.html',context)
     messages.info(request,'please login')
     return redirect('login')

@session_handler
def checkout(request, username=None):
    if username:
        cart_obj, created = Order.objects.get_or_create(
            owner=username,
            order_status=Order.CART_STAGE
        )
        cartid = Order.objects.filter(owner=username)
        print(cartid)
        if request.method=='POST':
                                total_str=request.POST["total"]
                                total_float=float(total_str)
                                total=int(total_float)

       

        return redirect('paymentstatus')
    
@session_handler
def conform(request, username=None):
    if username:
        cart_obj, created = Order.objects.get_or_create(
            owner=username,
            order_status=Order.CART_STAGE
        )
        address = Address.objects.filter(user=username).first()
        
        if address:
            print(address)
            
            if request.method == 'POST':
                total_str = request.POST["total"]
                try:
                    total_float = float(total_str)
                    total = int(total_float)
                except ValueError:
                    print("The total amount must be a valid number.")
                    return redirect('some_error_page')  # Redirect to an error page if needed

                payment = client.order.create({
                    "amount": total * 100,  # Amount in paise for Razorpay
                    "currency": "INR",
                    "payment_capture": "1"
                })
                print(payment)

                order_id = payment['id']
                order_status = payment['status']
                
                if order_status == 'created':
                    payment = Payment(
                        user=username,
                        amount=total,
                        razorpay_order_id=order_id,
                        razorpay_payment_status=order_status
                    )
                    payment.save()
                
                    order_obj = Order.objects.get(
                        owner=username,
                        order_status=Order.CART_STAGE,
                    )
                    if order_obj:
                          order_obj.total_price = total
                          order_obj.save()


                    checkout = Checkout(
                        user_id=username,
                        orderid=order_id,
                        sub_total=total,
                        order=order_obj,
                        payable_amount=total,
                        phone=username.number  # Make sure `username` has a `number` attribute
                        )
                    checkout.save()
                        

                    wish=Wishlist.objects.all()
                    context = {
                        'cart': cart_obj,
                        'address': address,
                        'total': total,
                        'user': username,
                        'order_id': order_id,
                        'wish':wish,
                        'username':username
                    }
                    return render(request, 'cart/checkout.html', context)
            else:
                return render(request, 'userprofile/addaddress.html')
        else:
            return render(request, 'userprofile/addaddress.html')
    else:
        return redirect('index')

     


@csrf_exempt
def success(request):
             try:
                response=request.POST
                print(response)
                params_dict={
                    'razorpay_payment_id': response['razorpay_payment_id'],
                    'razorpay_order_id': response['razorpay_order_id'],
                    'razorpay_signature': response['razorpay_signature']

                }

                print(params_dict)
                client=razorpay.Client(auth=('rzp_test_MrcFBm65u39qex','HsMWRqSflka9cs5l0EwuyxTZ'))
                try:
                    status=client.utility.verify_payment_signature(params_dict)
                    payment=Payment.objects.get(razorpay_order_id=response['razorpay_order_id'])
                    payment.razorpay_payment_id=response['razorpay_payment_id']
                    payment.paid=True
                    payment.save()
                    checkout=Checkout.objects.get(orderid=response['razorpay_order_id'])
                    checkout.status=Checkout.ACCEPTED
                    checkout.paymentid=response['razorpay_payment_id']
                    checkout.paid=True
                    checkout.paymentmode="Razorpay"
                    checkout.save()

                    return redirect('paymentstatus')
                except:
                    return render(request,'userprofile/ordertrack.html')
             except:
                  return render(request,'userprofile/paymentfail.html')

@session_handler
def cancelorder(request,id,username=None):
    if username:
            cart_obj,created=Order.objects.get_or_create(
                owner=username,
                order_status=Order.CART_STAGE
            )
            pid=Orderitem.objects.get(id=id)
            print(pid)
            wish=Wishlist.objects.all()
            if username:
                context={
                    'username':username,
                    'pid':pid,
                    'wish':wish,
                    'cart':cart_obj
                }
                return render(request,'userprofile/ordercancel.html',context)
            return redirect('/')
    return redirect('login')

@session_handler
def cancelsubmit(request,pid,username=None):
    if username:
        if request.method=='POST':
            name=request.POST['firstname']
            email=request.POST['email']
            reson=request.POST['subject']
            item=Orderitem.objects.get(id=pid)
            item.item_status=Orderitem.ORDER_REJECTED
            item.save()
            cancel=Cancelorder(order=item,user=username,reason=reson)
            cancel.save()
            messages.success(request,'order canceled')
            return redirect('ordertrack')
    else:
         return redirect('index')


@session_handler
def paymentstatus(request,username=None):
    if username:
        cart_obj,created=Order.objects.get_or_create(
                owner=username,
                order_status=Order.CART_STAGE
            )
        
        order_obj = Order.objects.get(
                        owner=username,
                        order_status=Order.CART_STAGE,
                    )

        user=Order.objects.get(
                         owner=username,
                         order_status=Order.CART_STAGE,
                         )
        item_obj = Orderitem.objects.filter(
                        owner=user,
                        item_status=Order.CART_STAGE,
                    

                    )
        if order_obj:
                        address = Address.objects.filter(user=username).first()
                        order_obj.order_status = Order.ORDER_CONFIRMED
                        order_obj.address=address
                        order_obj.save()

        if item_obj:
                        for i in item_obj:
                            i.item_status=Orderitem.ORDER_CONFIRMED
                            i.save()
                        print(order_obj)

        address=Address.objects.get(user=username)
        wish=Wishlist.objects.all()
        context={
             'address':address,
             'wish':wish,
             'username':username,
             'cart':cart_obj
        }
        return render(request,'userprofile/thankyou.html',context)
    else: 
         return redirect('/')
    


