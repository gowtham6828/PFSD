from django.shortcuts import render
def homepage(request):
    return render(request,"index.html")
def loginPage(request):
    return render(request,"login.html")
def registrationPage(request):
    return render(request,"register.html")
def viewpackages(request):
    return render(request,"viewpackages.html")
def insertpackages(request):
    return render(request,"insertpackages.html")