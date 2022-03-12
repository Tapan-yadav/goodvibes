from django.shortcuts import render
from django.http import HttpResponse 
from index.models import Event , Contact

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def get(request):
    return render(request,'get.html')

def contact(request):
    if request.method == "POST":
        print("This is post")
        name = request.POST.get('name','')
        shop = request.POST.get('shop','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        location = request.POST.get('location','')
        message = request.POST.get('message','')

        contact = Contact(name = name , shop = shop , email = email, phone = phone , location = location, message = message)
        contact.save()

        print (name , shop, email,phone,location,message)
    return render(request,'contact.html')

def events(request):
    if request.method == "POST":
        print("This is a Post")
        name = request.POST.get('name','')
        shop = request.POST.get('shop','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        location = request.POST.get('location','')
        print(name,shop,email,phone,location)

        ins = Event(name = name , shop = shop , email = email, phone = phone , location = location)
        ins.save()
        print ("the data has been written to the db")
    return render(request, 'events.html')


