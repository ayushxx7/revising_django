from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        print(request.user)
        return render(request, 'index.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            return render(request, 'login.html')
        else:
            login(request, user=user)
            return redirect("/")
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')
