from django.core.exceptions import MiddlewareNotUsed
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import JsonResponse, request
from .models import Categories

# Create your views here.
def login(request):
    user = 'not logged in'
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        us = User.get_username
        if user is not None:
            # print(dir(request.session))
            request.session['user_id'] = user.id
            request.session['user_username'] = user.username
            user = request.session.get('session_key')
            return JsonResponse(
                {'success': True},
                safe=False
            )
        else:
            messages.info(request, "Invalid Credentials")
            # return redirect('')
            return JsonResponse(
                {'success': False},
                safe=False
            )
    else:
        user = request.session.get('user_username')
        print(user)
        if user is not None:
            print(user)
            return redirect('display')
        else:
            return render(request, 'user_login.html')

    

def register(request):
    if (request.method=='POST'):
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['email']
        username=request.POST['uname']
        
        password=request.POST['password']
        passwordcon=request.POST['passwordConfirmation']
        print(fname)
        if password == passwordcon:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                print("Username Already Exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already Used')
                print("Email Already Used")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=fname, last_name=lname, email=email, )
                user.save();
                print('success')
                return redirect('/')
        else:
            messages.info(request, 'Password is not matching...')
            print('Password is not matching...')
            return redirect('register')

    else:
        return render(request, 'registration.html')
       
 
def admin(request):
    if (request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        user = auth.authenticate(username=username,password=password,is_superuser=True, is_staff=True)
        
        if user is not None:
            request.session['user_id'] = user.id
            request.session['user_username'] = user.username
            user = request.session.get('session_key')
            return redirect('adminhome')
        else:
            return redirect('admin')
    else:
        user = request.session.get('user_username')
        print(user)
        if user is not None:
            print(user)
            return redirect('adminhome')
        else:
           return render(request, 'admin_login.html')

def view_user(request):
    user = User.objects.all()
    return render(request, 'view_user.html', {"users":user})

def display(request):
    return render(request, "display.html")

def viewcategory(request):
    cat_list=Categories.objects.all()
    return render(request, "categories.html",{"categories":cat_list} )

def adminhome(request):
    return render(request, 'adminhome.html')

def addcategory(request):
    category=request.POST['catergory']
    categories=Categories.objects.create(category=category)
    categories.save()

    return redirect('viewcategory')

def edituser(request):
    id=request.GET['id']
    if(request.method=='POST'):
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['email']
        username=request.POST['uname']
        password=request.POST['password']
        passwordcon=request.POST['passwordConfirmation']
        user = User.objects.get(id=id)
        user.first_name=fname
        user.last_name=lname
        user.email=email
        user.username=username
        user.password=password
        user.save();
        print('success')
        return redirect('view_user')
         
    else:
        
        user = User.objects.filter(id=id)
        print(user)
        print(id)
        return render(request,'edituser.html',{"users":user})

def deleteuser(request):
      id=request.GET['id']
      user = User.objects.filter(id=id)
      print(user)
      user.delete()
      return redirect('view_user')

def add_user(request):
    if (request.method=='POST'):
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['email']
        username=request.POST['uname']
        
        password=request.POST['password']
        passwordcon=request.POST['passwordConfirmation']
        print(fname)
        if password == passwordcon:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                print("Username Already Exist")
                return redirect('add_user')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already Used')
                print("Email Already Used")
                return redirect('add_user')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=fname, last_name=lname, email=email, )
                user.save();
                print('success')
                return redirect('view_user')
        else:
            messages.info(request, 'Password is not matching...')
            print('Password is not matching...')
            return redirect('add_user')

    else:
        
        return render(request,'adduser.html')



def logout(request):
    del request.session['user_username']
    # request.session.flush()
    
    
    return redirect('/') 
