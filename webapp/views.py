from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>HEY!</h2>")

def first(request):
	return HttpResponse("<h1>My First!!!</h1>")

def home(request):
	return render(request,'home.html')
def contact(request):
    return render(request, 'basic.html',{'content':['If you would like to contact me, please email me.','hskinsley@gmail.com']})