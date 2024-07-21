from django.shortcuts import redirect, render,reverse

from home.decorator import session_handler
from order.models import Order, Wishlist
from product.models import Filter_Price, Product_review, Products
from category.models import Category
from product.models import Products
from home.models import Customuser
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Avg
from django.db.models import Q, Sum
from order.views import checkwishlist



# Create your views here.
@session_handler
def singleproduct(request,id,username=None):
    product=Products.objects.get(id=id)
    avgrate=product.reviews.aggregate(Avg('ratings'))['ratings__avg']
    print(avgrate)
    reviews=Product_review.objects.filter(item=id)
    review_count=Product_review.objects.filter(item=id).count()

    related=Products.objects.filter(category=product.category).exclude(pk=id)[:5]
    product.views+=1
    product.save()
    if username:
        cart_obj,created=Order.objects.get_or_create(
                    owner=username,
                    order_status=Order.CART_STAGE
                )
        wish=Wishlist.objects.all()
        in_wish=checkwishlist(username,id)
        context={
            'product':product,
            'related':related,
            'reviews':reviews,
            'avg':avgrate,
            'cart':cart_obj,
            'username':username,
            'in_wish':in_wish,
            'wish':wish,
            'review_count':review_count
        }
        return render(request,'shop/productdetails.html',context)
    else:
        context={
            'product':product,
            'related':related,
            'reviews':reviews,
            'avg':avgrate,
            'username':username

        }
        return render(request,'shop/productdetails.html',context)

    
    print(avg)
    return render(request,'shop/productdetails.html',context)




@session_handler
def review_page(request,id,username=None):
    if username:
         if request.method == "POST":
            star_rating=request.POST["your-review"]
            reviews=request.POST["opinion"]
            product = Products.objects.get(id=id)
            user=username
            print(user)
            review=Product_review(user=user,item=product,review_desp=reviews,ratings=star_rating)
            print(Product_review)
            review.save()
            return redirect(reverse('singleproduct', args=[id]))
         return redirect(reverse('singleproduct', args=[id]))
    messages.info(request,'please login')
    return redirect('login')


@session_handler
def allproduct(request,username=None):
    pro=Products.objects.filter().order_by('-views')
    procount=Products.objects.count()
    category=Category.objects.all()
    fprice=Filter_Price.objects.all()
    
    paginator=Paginator(pro,8)
    page_no=request.GET.get('page')
    product=paginator.get_page(page_no)
    if username:
            cart_obj,created=Order.objects.get_or_create(
                    owner=username,
                    order_status=Order.CART_STAGE
                )
            wish=Wishlist.objects.all()


            context={
                'product':product,
                'procount':procount,
                'category':category,
                'fprice':fprice,
                'cart':cart_obj,
                'username':username,
                'wish':wish
                
            }
            return render(request,'shop/allproduct.html',context)
    else:
            context={
                'product':product,
                'procount':procount,
                'category':category,
                'fprice':fprice,
            }
            return render(request,'shop/allproduct.html',context)


@session_handler
def filterprice(request,id,username=None):
            pro=Products.objects.filter(filter_price=id).order_by('price')
            procount=Products.objects.filter(filter_price=id).count()
            category=Category.objects.all()
            fprice=Filter_Price.objects.all()

            
            paginator=Paginator(pro,8)
            page_no=request.GET.get('page')
            product=paginator.get_page(page_no)
            if username:
                cart_obj,created=Order.objects.get_or_create(
                                owner=username,
                                order_status=Order.CART_STAGE
                            )
                wish=Wishlist.objects.all()
                context={
                            'product':product,
                            'procount':procount,
                            'category':category,
                            'fprice':fprice,
                            'cart':cart_obj,
                            'wish':wish,
                            'username':username
                            
                        }
                return render(request,'shop/allproduct.html',context)
            else:
                 context={
                            'product':product,
                            'procount':procount,
                            'category':category,
                            'fprice':fprice,
                            'username':username
                            
                        }
                 return render(request,'shop/allproduct.html',context)

@session_handler
def filterstock(request,id,username=None):
            pro=Products.objects.filter(stock=id)
            procount=Products.objects.filter(stock=id).count()
            category=Category.objects.all()
            fprice=Filter_Price.objects.all()
            
            paginator=Paginator(pro,8)
            page_no=request.GET.get('page')
            product=paginator.get_page(page_no)
            if username:
                cart_obj,created=Order.objects.get_or_create(
                                owner=username,
                                order_status=Order.CART_STAGE
                            )
                wish=Wishlist.objects.all()
                context={
                            'product':product,
                            'procount':procount,
                            'category':category,
                            'fprice':fprice,
                            'cart':cart_obj,
                            'wish':wish,
                            'username':username
                            
                        }
                return render(request,'shop/allproduct.html',context)
            else:
                 context={
                            'product':product,
                            'procount':procount,
                            'category':category,
                            'fprice':fprice,
                            'username':username
                            
                        }
                 return render(request,'shop/allproduct.html',context)



           

@session_handler
def filtercategory(request,id,username=None):
    categeory=Category.objects.get(id=id)
    pro=Products.objects.filter(category=categeory)
    procount=Products.objects.filter(category=categeory).count()
    category=Category.objects.all()
    fprice=Filter_Price.objects.all()

    paginator=Paginator(pro,8)
    page_no=request.GET.get('page')
    product=paginator.get_page(page_no)
    if username:
        cart_obj,created=Order.objects.get_or_create(
                    owner=username,
                    order_status=Order.CART_STAGE
                )
        wish=Wishlist.objects.all()

        context={
            'product':product,
            'procount':procount,
            'category':category,
            'fprice':fprice,
            'categeory':categeory,
            'cart':cart_obj,
            'wish':wish,
            'username':username
        }
        return render(request,'shop/allproduct.html',context)
    else:
        context={
            'product':product,
            'procount':procount,
            'category':category,
            'fprice':fprice,
            'categeory':categeory,
            'username':username
        }
        return render(request,'shop/allproduct.html',context)
         

     


@session_handler
def search(request,username=None):
        query = request.GET.get('query')
        procount=Products.objects.count()
        p=Products.objects.all()
        prod= Products.objects.filter(Q(name__contains=query) | Q(desc__contains=query) | Q(offer__contains=query))

        paginator=Paginator(prod,8)
        page_no=request.GET.get('page')
        product=paginator.get_page(page_no)
        print(product)
        if username:
                cart_obj,created=Order.objects.get_or_create(
                        owner=username,
                        order_status=Order.CART_STAGE
                    )
                wish=Wishlist.objects.all()

                if not product:
                    msg='No results found'
                    context = {
                        'msg':msg
                    }
                    context={
                        'procount':procount,
                        'msg':msg,
                        'cart':cart_obj,
                        'wish':wish,
                        'username':username

                    }
                    return render(request,'shop/search.html',context)
                else:
                    msg='search result'
                    context = {
                        'msg':msg
                    }
                    context={
                        'product':product,
                        'procount':procount,
                        'msg':msg,
                        'cart':cart_obj,
                        'wish':wish,
                        'username':username
                    }
                    return render(request,'shop/search.html',context)
        else:
                if not product:
                    msg='No results found'
                    context = {
                        'msg':msg
                    }
                    context={
                        'procount':procount,
                        'msg':msg,
                        'cart':cart_obj

                    }
                    return render(request,'shop/search.html',context)
                else:
                    msg='search result'
                    context = {
                        'msg':msg
                    }
                    context={
                        'product':product,
                        'procount':procount,
                        'msg':msg,
                        'cart':cart_obj
                    }
                    return render(request,'shop/search.html',context)


@session_handler
def prodcategory(request,id,username=None):
    categeory=Category.objects.get(id=id)
    pro=Products.objects.filter(category=categeory)
    procount=Products.objects.filter(category=categeory).count()
    category=Category.objects.all()
    fprice=Filter_Price.objects.all()

    paginator=Paginator(pro,8)
    page_no=request.GET.get('page')
    product=paginator.get_page(page_no)
    if username:
                cart_obj,created=Order.objects.get_or_create(
                            owner=username,
                            order_status=Order.CART_STAGE
                        )
                wish=Wishlist.objects.all()

                context={
                'product':product,
                'procount':procount,
                'category':category,
                'fprice':fprice,
                'categeory':categeory,
                'cart':cart_obj,
                'wish':wish,
                'username':username
                }
                return render(request,'shop/categoryproduct.html',context)
    else:
                context={
                'product':product,
                'procount':procount,
                'category':category,
                'fprice':fprice,
                'categeory':categeory,
                'username':username
                }
                return render(request,'shop/categoryproduct.html',context)





@session_handler
def removereview(request,id ,username=None):
    if username:
        try:
            review=Product_review.objects.filter(user=username)
            if review:
                r=Product_review.objects.get(id=id)
                r.delete()
                return redirect(request.META.get('HTTP_REFERER'))
            return redirect(request.META.get('HTTP_REFERER'))
        except Exception as e:
            return redirect(request.META.get('HTTP_REFERER'))

