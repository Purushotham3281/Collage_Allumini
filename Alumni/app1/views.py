from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def profile(request):
    return render(request,"profile.html")

def more(request):
    return render(request,"more.html")


def dedicate(request,rid):
    return render(request,"dedicate.html")

def loginView(request):
    return render(request,"login.html")

def register(request):
    return render(request,"register.html")

def update(request,rid):
    return render(request,"update.html")

def logoutView(request):
    return render(request,"home.html")

def delete(request,rid):
    return render(request,"staff.html")

def staff(request):
    return render(request,"staff.html")

