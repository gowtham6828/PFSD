from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .models import Admin,Register,Packages


def ttmhome(request):
    return render(request, "ttmhome.html")
def checkadminlogin(request):
    if request.method == "POST":
        adminuname = request.POST["uname"]  # gets user name
        adminpwd= request.POST["pwd"]
        flag = Register.objects.filter(name=adminuname, password=adminpwd).values()
        if flag:
            if adminuname == "ig":
                return render(request, "adminhome.html")
        if flag:
            return render(request, "ttmhome.html")
        else:
            return HttpResponse("Login Failed")
def checkregistration(request):
    if request.method =="POST":
        name =request.POST["name"]
        addr =request.POST["addr"]
        email = request.POST["email"]
        phno = request.POST["phno"]
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        cpwd = request.POST["cpwd"]

    if pwd == cpwd:
        if Register.objects.filter(username=uname).exists():
            messages.info(request,"username existing...")
            return render(request,"register.html")
        elif Register.objects.filter(email=email).exists():
            messages.info(request,"email existing...")
            return render(request,"registar.html")
        else:
            user = Register.objects.create(name=name,address=addr,email=email,phnumber=phno,username=uname,password=pwd)
            user.save()
            messages.info(request,"user created...")
            return render(request,"login.html")
    else:
        messages.info(request,"password doesn't match")
        return render(request,"register.html")
def checkpackages(request):
    if request.method == "POST":
        tcode = request.POST["tourcode"]
        tname = request.POST["tourname"]
        tpack = request.POST["tourpackage"]
        tdesc = request.POST["desc"]
        pack=Packages.objects.create(tourcode=tcode,tourname=tname,tourpackage=tpack,desc=tdesc)
        pack.save()
        messages.info(request,"data Inserted Sucessfully")
        return render(request,"package.html")
    else:
        messages.info(request, "Data Fail to  Inserted")
        return render(request, "package.html")
def viewplaces(request):
    data = Packages.objects.all()
    return render(request,"viewplaces.html",{"placesdata":data})
def checkChangePassword(request):
    if request.method == "POST":
        uname=request.POST["uname"]
        opwd=request.POST["opwd"]
        npwd=request.POST["npwd"]
        flag=Register.objects.filter(username=uname,password=opwd).values()
        if flag:
            Register.objects.filter(username=uname,password=opwd).update(password=npwd)
            messages.info(request, "password updated")
            return render(request,"index.html")
    else:
        return render(request, "changepassword.html")
def logout(request):
    messages.info(request,"logout")
    return render(request,"index.html")

