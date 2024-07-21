from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from.import views


urlpatterns = [
path('addcart/<int:id>',views.addcart,name='addcart'),
path('addwish/<int:id>',views.add_to_wish,name='addwish'),
path('removewish/<int:id>',views.removewish,name='removewish'),
path('wishlist',views.wishlist,name='wishlist'),
path('quickaddcart/<int:id>',views.quickaddcart,name='quickaddcart'),
path('quickaddwish/<int:id>',views.quickaddwish,name='quickaddwish'),

path('removeitem/<int:id>',views.removeitem,name='removeitem'),
path('checkout',views.checkout,name='checkout'),
path('success/',views.success,name='success'),
path('ordercancel/<int:id>/',views.cancelorder,name='ordercancel'),
path('paymentstatus',views.paymentstatus,name='paymentstatus'),
path('conform',views.conform,name='conform'),
path('cancelsubmit/<int:pid>/',views.cancelsubmit,name='cancelsubmit')

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)