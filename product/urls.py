from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from.import views


urlpatterns = [
    path('singleproduct/<int:id>/',views.singleproduct,name='singleproduct'),
    path('review_page/<int:id>/',views.review_page,name='review_page'),
    path('allproduct',views.allproduct,name='allproduct'),
    path('prodcategory/<int:id>',views.prodcategory,name='prodcategory'),
    path('removereview/<int:id>/',views.removereview,name='removereview'),
    path('search/',views.search,name='search'),
    path('filterprice/<int:id>',views.filterprice,name='filterprice'),
    path('filtercategory/<int:id>',views.filtercategory,name='filtercategory'),
    path('filterstock/<int:id>',views.filterstock,name='filterstock')



]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)