from django.shortcuts import render,redirect

from category.models import Category
from order.models import Order, Wishlist
from product.models import Products
from .decorator import session_handler
from home.models import Customuser
from django.contrib import messages
from django.core.mail import send_mail
import random

import http.client

from django.conf import settings



# Create your views here.

@session_handler
def index(request,username=None):
    product=Products.objects.filter().order_by('-id')[:8]
    category=Category.objects.all()
    offer=Products.objects.order_by('-offer').first()
    print(offer)

    if username:
        cart_obj,created=Order.objects.get_or_create(
            owner=username,
            order_status=Order.CART_STAGE
        )
        wish=Wishlist.objects.all()

        context={
            'username':username,
            'category':category,
            'product':product,
            'offer':offer,
            'cart':cart_obj,
            'wish':wish
        }
        return render(request,'index.html',context)
    else:
        context={
            'category':category,
            'product':product,
            'offer':offer
        }
        return render(request,'index.html',context)

@session_handler
def about(request,username=None):
    if username:
        cart_obj,created=Order.objects.get_or_create(
                owner=username,
                order_status=Order.CART_STAGE
            )
        wish=Wishlist.objects.all()
        context={
            'wish':wish,
            'cart':cart_obj,
            'username':username
        }
        return render(request,'about.html',context)
    
    else:
        cart_obj,created=Order.objects.get_or_create(
                owner=username,
                order_status=Order.CART_STAGE
            )
        wish=Wishlist.objects.all()
        context={
            'wish':wish,
            'cart':cart_obj,
        }
        return render(request,'about.html',context)

@session_handler   
def newitem(request,username=None):
    category=Category.objects.all()
    product=Products.objects.filter().order_by('-id')[:8]
    offer=Products.objects.order_by('-offer').first()
    if username:
        cart_obj,created=Order.objects.get_or_create(
                    owner=username,
                    order_status=Order.CART_STAGE
                )
        wish=Wishlist.objects.all()
        context={
                'category':category,
                'product':product,
                'offer':offer,
                'cart':cart_obj,
                'username':username,
                'wish':wish
            }
        return render(request,'index.html',context)
    else:
        context={
                'category':category,
                'product':product,
                'offer':offer,
            }
        return render(request,'index.html',context)

        

@session_handler
def popular(request,username=None):
    product=Products.objects.filter().order_by('-views')[:8]
    category=Category.objects.all()
    offer=Products.objects.order_by('-offer').first()
    if username:
        cart_obj,created=Order.objects.get_or_create(
                    owner=username,
                    order_status=Order.CART_STAGE
                )
        wish=Wishlist.objects.all()
        context={
                'category':category,
                'product':product,
                'offer':offer,
                'cart':cart_obj,
                'username':username,
                'wish':wish

            }
        return render(request,'index.html',context)
    else:
        context={
                'category':category,
                'product':product,
                'offer':offer,
            }
        return render(request,'index.html',context)


@session_handler
def login(request,username=None):
    wish=Wishlist.objects.all()
    context={
        'wish':wish
    }
    return render(request,"login/login.html",context)

def register(request):
    wish=Wishlist.objects.all()
    context={
        'wish':wish
    }
    return render(request,'login/register.html',context)


@session_handler
def signin(request,username=None):
    if username:
        return redirect('/')
    try:
        if request.method == "POST":
            email = request.POST["email"]
            password = request.POST["password"]
            try:
                user = Customuser.objects.get(email=email, password=password)
            except Customuser.DoesNotExist or Customuser.MultipleObjectsReturned:
                user = None
            if user is not None:
                if user.is_blocked == True:
                    messages.error(request, "You are blocked ")
                    return redirect("login")

                if user.is_verified == True:
                    request.session["users"] = email
                    u1=user.first_name
                    messages.success(request, f'Login success welcome {u1}')
                    return redirect("/")
            else:
                messages.error(request, "invalid username or password")
                return redirect("login")
    except Exception as e:
        print(e)
    return render(request,'login/login.html')



@session_handler
def signup(request,username=None):
    if username:
        return redirect("index")
    try:
        if request.method == "POST":
            fname = request.POST["fname"]
            lname = request.POST["lname"]
            email = request.POST["email"]
            phone = request.POST["phone"]
            password = request.POST["password"]
            image=request.FILES["imageUpload"]

            if Customuser.objects.filter(email=email).exists():
                messages.error(request, "Email already exists you can login ")
                return redirect("login")
            
            if Customuser.objects.filter(number=phone).exists():
                messages.error(request, "Phone number already exists you can login ")
                return redirect("login")
            if not(2<= len(fname)):
                messages.error(request, "first name containe at least 2 characters long")
                return redirect("register")
            
            if not(2<= len(lname)):
                messages.error(request, "last name containe at least 2 characters long")
                return redirect("register")
            
            if len(phone) != 10:
                messages.error(request, "Enter a valid number")
                return redirect("register")

            if not password.strip() :
                messages.error(request, "Enter valid Password")
                return redirect("register")
            if len(password) < 6:
                messages.error(
                    request, " Password length too short minimum 6 chararcters"
                )
                return redirect("register")
            phone=int(phone)
            otp = str(random.randint(1000 , 9999))
            user = Customuser(
               first_name=fname.strip(), last_name=lname.strip(), email=email, number=phone,password=password.strip(),profilepic=image,otp=otp
            )
            
            # user.is_verified=True
            sendotp(email,otp)
            user.save()
            messages.success(request, "Registered successfully now verify,4 digit code send to your number")
            id=user.id
            context={
                'userid':id
            }
            return render(request,"login/verification.html",context)
        
    except Exception as e:
        print(e)

    return render(request, "login/register.html")




def sendotp(mail,otp):
    try:
        otp=otp
        subject='your otp code'
        msg=f'Green Life | indoor plants , your otp code is {otp}'
        email_from=settings.EMAIL_HOST_USER
        recipient_list=[mail]

        send_mail(subject,msg,email_from,recipient_list)
    except:
        print('error')


def verify(request):
    if "users" in request.session:
        return redirect("/")
    try:
            if request.method == "POST":

                otp = request.POST["otp"]
                user_id = request.POST["userid"]
                user_otp=int(otp)
                print(user_otp)
                try:
                    tb_user = Customuser.objects.get(id=user_id)
                except Customuser.DoesNotExist:
                    tb_user = None
                    
                print(tb_user.otp)

                if tb_user.otp == user_otp:
                    if tb_user.is_verified:
                        userid=tb_user.id
                        print(userid)
                        context={
                            'userid':userid
                        }
                        return render(request, "login/resetpass.html",context)
                        

                    else:
                        tb_user.is_verified = True
                        tb_user.save()
                        request.session["users"] = tb_user.email
                        u=tb_user.first_name
                        n=tb_user.last_name
                        nu=n+u
                        messages.success(request, f"Login successfully, {nu}")
                        return redirect("/")
                else:
                    messages.error(request, "Invalid otp Try again!")
                    context={
                        'userid':user_id
                    }
                    return render(request,"login/verification.html",context)


            return render(request, "login/verification.html")

    except Exception as e:
        print(e)

    return redirect("register")



@session_handler
def forgetpass(request,username=None):
        return render(request,'login/forgetpass.html')

def forgetpassword(request):
    try:
        if request.method == "POST":
            mail = request.POST["mail"]
            try:
                user1 = Customuser.objects.get(email=mail)
            except:
                messages.error(request, "enter registered mail id")
                return redirect("forgetpass")

            if user1 is not None:
                otp = str(random.randint(1000 , 9999))
                email=user1.email
                user1.otp=otp
                user1.save()
                messages.success(request, "Conform your mail id using the OTP")
                sendotp(email,otp)
                userid=user1.id
                context={
                'userid':userid
                    }
                return render(request,"login/verification.html",context)

    except Exception as e:
        print(e)

    messages.error(request, "enter registered email id")
    return redirect("forgetpass")

    # if username:
    #     user=Customuser.objects.get(user=username)
    #     phone=user.number
    #     otp = str(random.randint(1000 , 9999))
    #     user.otp=otp
    #     user.save()
    #     sendotp(phone,otp)
    #     messages.info(request,'4 digit code send to your number')
    #     user_id=user.id
    #     context={
    #                     'userid':user_id
    #                 }
    #     return render(request,"login/verification.html",context)
    # messages.info(request,'please login')
    # return redirect('login')


def resetpass(request):
    if request.method=='POST':
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        userid=request.POST['userid']
        if pass1==pass2:
             if len(pass1) < 6:
                context={
                    'userid':userid
                    }
                messages.error(request, " Password length too short minimum 6 chararcters")
                return render(request, "login/resetpass.html",context)
             user=Customuser.objects.get(id=userid)
             user.password=pass1
             user.save()
             messages.success(request,'Password change successfully,Now you can login')
             return redirect('login')
        else:
            messages.error(request,'password missmatch')
            context={
                    'userid':userid
                    }
            return render(request, "login/resetpass.html",context)


def logout(request):
    if "users" in request.session:
        del request.session["users"]
    messages.info(request,'Logout')
    return redirect("login")

