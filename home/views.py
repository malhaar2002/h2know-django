from django.shortcuts import render, redirect
from requests import request
from home.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def home(request):
    context = {'user': request.session['user']}
    return render(request, 'index.html', context)

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try:
            obj = User.objects.filter(email = email).first()
            if check_password(password, obj.password):
                request.session['user'] = email
                return redirect('dashboard')
            else:
                messages.info(request, 'Incorrect Password')
        except:
            messages.info(request, 'User does not exist. Try creating an account')

    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        fullName = request.POST['fullname']
        floorNo = request.POST['floorno']
        email = request.POST['email']
        password = request.POST['password']
        encrypted_password = make_password(password)
        totalVolume = 0
        obj = User(fullName, floorNo, email, encrypted_password, totalVolume)
        obj.save()
        return redirect('login')

    return render(request, 'register.html')

def dashboard(request):
    obj = User.objects.filter(email = request.session['user']).first()
    d = vol_find()
    dt = floor_data()
    context = {'d':d, 'dt':dt, 't_d':[600-dt[2], dt[2]], 'fullname':obj.fullName, 'floorno':obj.floorNo, 'email':obj.email, 'volume':d[1]}
    return render(request, 'dashboard.html', context)

def vol_find():
    f = open("vol_data.txt","r")
    vol = float(f.read())
    f.close()

    target = 60 #mention this in the site

    return [target-vol, vol]

def floor_data():
    f = open("floor_data.txt","r")
    dt = list((f.read()).split(" "))
    for i in range(len(dt)):
        dt[i] = float(dt[i])
    f.close()

    return dt

def logout(request):
    try:
        request.session['user'] = ''
        return home(request)
    except:
        return home(request)