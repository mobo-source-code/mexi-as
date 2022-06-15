from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def signup(request):
    if request.method == 'POST' : 
        username = request.POST.get('username')
        email = request.POST.get('email')
        full_name = request.POST.get('nom_complet')
        role = request.POST.get('role')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            user = User.objects.create(username=username, email=email, nom_complet=full_name, role=role, password=password1)
            login(request, user)
            return redirect('home')
        else: 
            return messages.error(request, 'Les mots de passes ne sont pas identiques')
    
    return render(request, 'registration/signup.html')

