from django.shortcuts import redirect, render
from home.decorator import session_handler
from home.models import Customuser
from django.contrib import messages

from order.models import Checkout, Order, Orderitem, Wishlist
from .models import Address, Contactus



# Create your views here.
@session_handler
def userprofile(request,username=None):
    if username:
        cart_obj,created=Order.objects.get_or_create(
                    owner=username,
                    order_status=Order.CART_STAGE
                )
        wish=Wishlist.objects.all()

        addresslength=Address.objects.filter(user=username).count()
        context={
            'username':username,
            'length':addresslength,
            'cart':cart_obj,
            'wish':wish
                 }
    return render(request,"userprofile/user_details.html",context)

@session_handler
def address(request,username=None):
    if username:
        cart_obj,created=Order.objects.get_or_create(
                    owner=username,
                    order_status=Order.CART_STAGE
                )
        wish=Wishlist.objects.all()
        context={
            'username':username,
            'cart':cart_obj,
            'wish':wish
        }
    return render(request,"userprofile/addaddress.html",context)

@session_handler    
def viewaddress(request,username=None):
    if username:
        cart_obj,created=Order.objects.get_or_create(
                    owner=username,
                    order_status=Order.CART_STAGE
                )
        add=Address.objects.get(user=username)
        addid=add.id
        print(addid)
        addresslength=Address.objects.filter(user=username).count()
        wish=Wishlist.objects.all()

        context={
                'address':add,
                'length':addresslength,
                'wish':wish,
                'cart':cart_obj,
                'addid':addid,
                'username':username
            }
        return render(request,"userprofile/addaddress.html",context)
    else:
        return redirect('addaddress')
        
@session_handler
def updateaddress(request,id,username=None):
    if username:
        cart_obj,created=Order.objects.get_or_create(
                    owner=username,
                    order_status=Order.CART_STAGE
                )
        add=Address.objects.get(id=id)
        addid=add.id
        print(addid)
        addresslength=Address.objects.filter(user=username).count()
        wish=Wishlist.objects.all()

        context={
                'address':add,
                'length':addresslength,
                'wish':wish,
                'cart':cart_obj,
                'addid':addid,
                'username':username
            }
        return render(request,"userprofile/updateaddress.html",context)
    else:
        return redirect('addaddress')

@session_handler
def updateuseraddress(request,username=None):
    if username:
            if request.method == "POST":
                name=request.POST['name']
                country=request.POST['country']
                state=request.POST['state']
                district=request.POST['dis']
                city=request.POST['city']
                pin=request.POST['pin']
                land=request.POST['land']
                addid=request.POST['addid']
                cart_obj,created=Order.objects.get_or_create(
                        owner=username,
                        order_status=Order.CART_STAGE
                    )
                addresslength=Address.objects.filter(user=username).count()
                wish=Wishlist.objects.all()
                add=Address.objects.get(id=addid)
                context={
                            'address':add,
                            'length':addresslength,
                            'wish':wish,
                            'cart':cart_obj,
                            'addid':addid,
                            'username':username
                        }
                
                if len(pin)!=6:
                    messages.error(request,'Enter valid pincode')
                    return render(request,"userprofile/updateaddress.html",context)
                print(name,country)
                add.name=name
                add.country=country
                add.state=state
                add.district=district
                add.city=city
                add.landmark=land
                add.pincode=pin
                add.user=username
                add.save()
                messages.success(request, "address updated")
                return redirect('userprofile')

            else:
                return redirect('addaddress')
    return redirect('address')


@session_handler
def addaddress(request,username=None):
    if username:
            if request.method == "POST":
                name=request.POST['name']
                country=request.POST['country']
                state=request.POST['state']
                district=request.POST['dis']
                city=request.POST['city']
                pin=request.POST['pin']
                land=request.POST['land']
                context={
                    'address':address
                }
                if len(pin)!=6:
                    messages.error(request,'Enter valid pincode')
                    return redirect('address')
                print(name,country)

                add=Address(name=name,country=country,state=state,city=city,district=district,pincode=pin,landmark=land)
                add.user=username
                add.save()
                messages.success(request, "New Address added successfully")
                return redirect('userprofile')
            else:
                return redirect('addaddress')
    return redirect('address')

@session_handler      
def deleteaddress(request,username=None):
    if username:
        address=Address.objects.get(user=username)
        address.delete()
        messages.info(request,'address deleted')
        return redirect('userprofile')






@session_handler
def updateprofile(request,username=None):
    if username:
        cart_obj,created=Order.objects.get_or_create(
                    owner=username,
                    order_status=Order.CART_STAGE
                )
        wish=Wishlist.objects.all()

        context={'username':username,'cart':cart_obj,'wish':wish}
    return render(request,"userprofile/updateprofile.html",context)


def editprofile(request,id):

    print(id)
    try:
        try:
            username = Customuser.objects.get(id=id)
        except Customuser.DoesNotExist:
            username = None

        context = {
            "username": username,
        }
        if request.method == "POST":
            fname = request.POST["update_fname"]
            lname = request.POST["update_lname"]
            number = request.POST["update_number"]
            if not number == "" and len(number) != 10:
                messages.error(request, "Enter valid number")
                return redirect("editprofile", id)

            username.first_name = fname
            username.last_name = lname
            username.number = number

            username.save()
            messages.success(request, "Profile Updated successfully ")
            return redirect('userprofile')
        return render(request,'userprofile/updateprofile.html',context)
    except Exception as e:
        print(e)
    return redirect("userprofile")


@session_handler
def ordertrack(request,username=None):
    try:
        if username:
            cart_obj,created=Order.objects.get_or_create(
                    owner=username,
                    order_status=Order.CART_STAGE
                )
            wish=Wishlist.objects.all()

            try:
                # allorder = Order.objects.filter(owner=username).exclude(order_status=Order.CART_STAGE).order_by("-id")
                    allorder=Orderitem.objects.all().exclude(item_status=Order.CART_STAGE).order_by("-id")
            except Exception as e:
                print(e)

            context = {
                "allorder": allorder,
                "username": username,
                'cart':cart_obj,
                'username':username,
                'wish':wish
            }
            return render(request, "userprofile/ordertrack.html", context)

    except Exception as e:
        print(e)
        return redirect("home")
    return redirect("login")


@session_handler
def orderitems(request, id, username=None):
    print(id)
    if username:
        cart_obj,created=Order.objects.get_or_create(
                    owner=username,
                    order_status=Order.CART_STAGE
                )
        wish=Wishlist.objects.all()

        try:
               # allorder = Order.objects.filter(owner=username).exclude(order_status=Order.CART_STAGE).order_by("-id")
                allorder=Orderitem.objects.get(id=id)
        except Exception as e:
                print(e)

        context = {
                "allorder": allorder,
                "username": username,
                'cart':cart_obj,
                'username':username,
                'wish':wish
            }
        return render(request, "userprofile/orderitemss.html", context)


       
    else:
        return redirect("login")




@session_handler
def myorders(request,username=None):
    if username:
        cart_obj,created=Order.objects.get_or_create(
            owner=username,
            order_status=Order.CART_STAGE
        )
        wish=Wishlist.objects.all()

        context={
            'cart':cart_obj,
            'wish':wish,
            'username':username
        }
        return render(request,'userprofile/myorders.html',context)
    return redirect('login')


@session_handler
def navbarcart(request,username=None):
    if username:
        cart_obj,created=Order.objects.get_or_create(
            owner=username,
            order_status=Order.CART_STAGE
        )
        wish=Wishlist.objects.all()

        context={
            'cart':cart_obj,
            'wish':wish
        }
        return render(request,'userprofile/myorders.html',context)
    return redirect('login')

def wishlist(request):
    return render(request,"userprofile/wishlist.html")

@session_handler
def contactform(request,username=None):
    if username:
        cart_obj,created=Order.objects.get_or_create(
                    owner=username,
                    order_status=Order.CART_STAGE
                )
        wish=Wishlist.objects.all()
        context={
            'wish':wish,
            'username':username,
            'cart':cart_obj
        }
        return render(request,'userprofile/contact.html',context)
    messages.info(request,'Please login')
    return redirect('login')

@session_handler
def contactus(request,username=None):
    if username:
        if request.method=='POST':
            name=request.POST['firstname']
            email=request.POST['email']
            msg=request.POST['subject']
            contact=Contactus(user=username,name=name,email=email,msg=msg)
            contact.save()
            messages.success(request,'Your message successfully send,We will contact you')
            return redirect('/')
    return redirect('login')

