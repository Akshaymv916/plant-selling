from django.urls import path

from . import views

urlpatterns = [
    path('userprofile',views.userprofile,name='userprofile'),
    path('addaddress',views.addaddress,name='addaddress'),
    path('address',views.address,name='address'),
    path('deleteaddress',views.deleteaddress,name='deleteaddress'),
    path('viewaddress',views.viewaddress,name='viewaddress'),
    path('updateprofile',views.updateprofile,name='updateprofile'),
    path('updateaddress/<int:id>',views.updateaddress,name='updateaddress'),
    path('updateuseraddress',views.updateuseraddress,name='updateuseraddress'),
    path('editprofile/<int:id>/',views.editprofile,name='editprofile'),
    path('ordertrack',views.ordertrack,name='ordertrack'),
    path('orderitems/<int:id>',views.orderitems,name='orderitems'),
    path('myorders',views.myorders,name='myorders'),
    path('contact',views.contactform,name='contact'),
    path('contactus',views.contactus,name='contactus'),

]