from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import UserDetails

# Create your views here.

def login1(request):
  return HttpResponse("<h1>welcome to this page by shakthi</h1>")


def homepage(request):
  return render(request,"homepage.html")

def loginprocess(request):
  uname=request.POST.get("text1")
  upassword=request.POST.get("text2")
  if uname=="admin" and upassword =="pass333":
    # return render(request,"adminpage.html")
    return redirect("loaddata")
  else:
    return render(request,"homepage.html")

def adminpage(request):
  return render(request,"adminpage.html")


def loaddata(request):
  records= UserDetails.objects.all().values()
  dictionary1 ={"userrecords":records}
  return render (request,"adminpage.html",dictionary1)


def addrecordform(request):
  return render (request,"addrecord.html")


def addrecordprocess(request):
  uname = request.POST.get('text1')
  upass = request.POST.get('text2')
  user1 = UserDetails(username = uname,password =upass)
  user1.save()
  return redirect("loaddata")

def editform(request,uid):
  user = UserDetails.objects.filter(id= uid).first()
  dictionary1 ={"record": user}
  return render(request,"editform.html",dictionary1)

def editrecordprocess(request):
  uid=request.POST.get("text1")
  uname= request.POST.get("text2")
  upass= request.POST.get("text3")

  UserDetails.objects.filter(id= uid).update(username=uname,password=upass)
  return redirect("loaddata")

