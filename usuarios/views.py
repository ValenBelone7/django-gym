from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UsuarioRegistrationForm


def register(request):
    if request.method == 'POST':
        form = UsuarioRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UsuarioRegistrationForm()
    return render(request, 'usuarios/register.html', {'form': form})
