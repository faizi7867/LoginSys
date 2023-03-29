from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def home(request):
    return render(request,'home.html')


def login_fun(request):
    return render(request,'login.html')


def register_fun(request):
    return render(request,'register.html')


def login_read(request):
    user_name = request.POST['tbusername']
    user_password = request.POST['tbpassword']
    myuser = authenticate(username=user_name, password=user_password)
    if myuser is not None:
        login(request,myuser)
        return render(request,'index.html')
    else:
        return render(request,'login.html',{'data':'invalid username or password'})


def register_read(request):
    uname = request.POST['tbusername']
    useremail = request.POST['tbemail']
    userpswd = request.POST['tbpassword']
    user = User.objects.create_superuser(email=useremail, password=userpswd, username=uname)
    user.save()
    return render(request, 'index.html',{'name':user})


def logout_fun(request):
    logout(request)
    return redirect('home')