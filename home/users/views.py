from django.shortcuts import render, redirect 
from datetime import datetime
from django.contrib import auth

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        user = request.user
        now = datetime.now()
        greetings = "Bonjour"
        if now.hour > 16:
            greetings = "Bonsoir"
        context = {
            "greetings": greetings,
            "user": user 
        }
        return render(request, "users/index.html", context)
    else:
        return redirect("users:login")

def login(request):
    if request.user.is_authenticated:
        return redirect("users:index")
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return redirect("users:index")

        else:
            messages = {
                "text": "Nom d'utilisateur ou mot de passe incorrect.",
                "level": "danger"
            }
    else:
        messages = {}
    return render(request, "users/login.html", {"messages": messages})

def logout(request):
    auth.logout(request)
    return render(request, "users/logout.html")

