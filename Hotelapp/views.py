from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from models import Food, Room, Order, Menu,Starters
from datetime import datetime
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout


def welcome(request):
    return render(request,'Hotelapp/index.html',{})



@login_required(redirect_field_name='next',login_url='/Hotelapp/sign-in/')
def about(request):
    return render(request,'Hotelapp/about.html',{})

@login_required
def listfood(request):
    foods=Food.objects.all()
    return render(request,'Hotelapp/food.html',{'foods':foods})

@login_required
def listroom(request):
    rooms=Room.objects.all()
    return render(request,'Hotelapp/rooms.html',{'rooms':rooms})
@login_required
def liststarter(request):
    starters=Starters.objects.all()
    return render(request,'Hotelapp/starters.html',{'starters':starters})


@login_required
def contact(request):

    return render(request,'Hotelapp/contact.html',{})

def sign_in(request):
    if request.method == 'GET':
         return render(request,'Hotelapp/sign-in.html',{})

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
             print 'login success'
    # Login is successful
             return render(request, 'Hotelapp/index.html', {})
        else:
            print 'login failure'
    # Login Fail Send some message
            return render(request, 'Hotelapp/sign-in.html', {'error': 'Username or password Wrong'})






def sign_up(request):
    if request.method == 'GET':
        user=User.objects.all()
        return render(request,'Hotelapp/sign-up.html',{user:'users'})
    elif request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        emailid=request.POST['emailid']
        newuser=User.objects.create_user(email=emailid,username=username,password=password)
        newuser.save()
        return render(request,'Hotelapp/sign-up.html',{})



def user(request):
    user1=User.objects.create_user(email='khandu@gmail.com',username='test2',password='test1526')
    user1.save()
    return HttpResponse("user created successfully")



#This function helps to create order in the system
#If the request is GET we render the form to users
#If the request is POST we take in the data, Create respective room,food,order item
#Order page has login_required decorator which makes sure user logs in before order is created.
@login_required
def order(request):
    if request.method=='GET':
        foods = Food.objects.all()
        rooms = Room.objects.all()
        return render(request,'Hotelapp/orders.html',{'foods':foods,'rooms':rooms,'ordercomplete':False})
    elif request.method=='POST':
        foodid=request.POST['foods']
        fooditem=Food.objects.get(pk=foodid)
        roomid=request.POST['rooms']
        roomitem=Room.objects.get(pk=roomid)

        now=datetime.now()
        user_id=1
        neworder=Order(food_item=fooditem,room_type=roomitem,user_id=user_id,order_timestamp=now,status='In Progress')
        neworder.save()
        print neworder.id
        orders = Order.objects.all()
        return render(request, 'Hotelapp/orders.html', {'orders':orders,'ordercomplete':True})
        


def sendSimpleEmail(request):
   res = send_mail('Subject here', 'Here is the message.', 'khandu.shigihalli@gmail.com', ['kva.anusha@gmail.com'], fail_silently=False)
   return HttpResponse('%s'%res)

def logout_view(request):
    logout(request)
    #return HttpResponse('i am in login page')
    return HttpResponseRedirect('/Hotelapp/')