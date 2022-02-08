from django.http import  HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Robin

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    return render(request, "index.html", {'result': obj})

def rob(request):
    obj1=Robin.objects.all()
    return render(request, "index.html", {'res': obj1})

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     sub=x-y
#     div=x/y
#     mult=x*y
#     return render(request,"result.html",{'result':[res,sub,div,mult]})
