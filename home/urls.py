from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from.import views


urlpatterns = [
    path('',views.index,name='index'),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('logout',views.logout,name='logout'),
    path('about',views.about,name='about'),
    path('newitem',views.newitem,name='newitem'),
    path('popular',views.popular,name='popular'),
    path('verify',views.verify,name='verify'),
    path('forgetpass',views.forgetpass,name='forgetpass'),
    path('forgetpassword',views.forgetpassword,name='forgetpassword'),
    path('resetpass',views.resetpass,name='resetpass')


]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)