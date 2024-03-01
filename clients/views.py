from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'Vous êtes déconnecté.')
    return redirect('login')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user directly from the form
            login(request, user)  # Automatically authenticate the newly registered user
            messages.success(request, 'Votre compte a été créé avec succès.')
            return redirect('home')  # Redirect to the home page or any desired URL
    else:
        form = UserCreationForm()
    return render(request, 'authenticate/register_user.html', {'form': form})
