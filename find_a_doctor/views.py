from django.shortcuts import render, redirect
from django.http import HttpResponse
from find_a_doctor.models import Doctor
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        exists=User.objects.filter(username=username).exists()
        if not exists:
            user=User.objects.create_user(username, email, password)
            return render(request, "success_msg.html")
    return render(request, "signup.html")

def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/doctors/')
        else:
            return render(request, "invalidlogin.html")
    return render(request, "signin.html")

def signout(request):
    logout(request)
    return redirect('/')

@login_required
def doctors(request):
    doctors=Doctor.objects.all()
    return render(request, "doctors.html", {"doctors":doctors})

@login_required
def doctor(request, name):
    doctor=Doctor.objects.get(name=name)
    return render(request, "doctor.html", {"doctor":doctor})

@login_required
def book(request, name):
    doctor=Doctor.objects.get(name=name)
    doctor.booked += 1
    doctor.save()
    print(doctor.booked)
    username=request.user.username
    email=request.user.email
    message = username + email
    msg = EmailMessage("Appointment", message, to=["priyankaraju22@gmail.com"])
    msg.send()
    return render(request, "booking_success.html")   

@login_required  
def add_doctor(request):
    if request.method=="POST":
        name=request.POST["name"]
        qualification=request.POST["qualification"]
        address=request.POST["address"]
        experience=request.POST["experience"]
        fee=request.POST["fee"]
        available=request.POST["available"]
        new=Doctor.objects.create(name=name, qualification=qualification, address=address, experience=experience, fee=fee, available=available)
        return redirect("/doctors/")
    return render(request, "add_doctor.html")

@login_required
def edit(request, name):
    doctor=Doctor.objects.get(name=name)
    if request.method=="POST":
        name=request.POST["name"]
        qualification=request.POST["qualification"]
        address=request.POST["address"]
        experience=request.POST["experience"]
        fee=request.POST["fee"]
        available=request.POST["available"]
        doctor.name=name
        doctor.qualification=qualification
        doctor.address=address
        doctor.experience=experience
        doctor.fee=fee
        doctor.available=available
        doctor.save()
        return redirect("/doctors/")
    return render(request, "edit.html", {"doctor":doctor})

@login_required
def remove(request, name):
    doctor=Doctor.objects.get(name=name)
    doctor.delete()
    return redirect("/doctors/")

def Chart(request):
    doctors=Doctor.objects.all()
    return render(request, "chart.html", {"doctors":doctors})

