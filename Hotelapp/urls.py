
from django.conf.urls import url,include
from django.contrib import admin
from views import welcome, listfood,listroom,liststarter,order,contact,sign_in,sign_up,about,user,sendSimpleEmail,logout_view

urlpatterns = [
    url(r'^$', welcome),
    url(r'food/',listfood),
    url(r'rooms/',listroom),
    url(r'starters/',liststarter),
    url(r'order/',order),
    url(r'contact/',contact),
    url(r'sign-in/',sign_in),
    url(r'sign-up/',sign_up),
    url(r'about/',about),
    url(r'user/',user),
    url(r'logout/', logout_view),
    url(r'Email/',sendSimpleEmail)


]
