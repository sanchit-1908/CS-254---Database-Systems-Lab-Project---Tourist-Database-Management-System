from django.shortcuts import render,HttpResponse

from itme.models import Category,item

# Create your views here.

def index(request):
    # return HttpResponse("this is home page .")
    
    items = item.objects.filter(isSold= False)[0:6]
    categories = Category.objects.all()
      
    return render(request,'index.html',{'categories':categories,'item' : items,})

def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")

def login(request):
    return render(request,"login.html")

def choice_of_login_page(request):
    return render(request,"choice_of_login_page.html")

def profile(request):
    return render(request,"profile.html")