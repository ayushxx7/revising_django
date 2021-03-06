from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return HttpResponse("This is Services Page")

def contact(request):
    print('trigger contact')
    print(request)
    if request.method == "POST":
        print('post request')
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = Contact(name=name, email=email, date=datetime.today())
        print('name:', name, 'email:', email)
        contact.save()
        messages.success(request, f'{name} saved!')
        print('saved to db')

    return render(request, 'contact.html')
