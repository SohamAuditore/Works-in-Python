from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    context = {
        'variable1' : "this is sent",
        'variable2' : "this is value sent",
        'variable3' : "this is character sent"
    }
    return render(request, 'index.html',context)
    #return HttpResponse("this is homepage") 

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is about page")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("This is the page showing the services offered")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Profile details updated.')

    return render(request, 'contact.html')
    #return HttpResponse("This is contact-us page")

