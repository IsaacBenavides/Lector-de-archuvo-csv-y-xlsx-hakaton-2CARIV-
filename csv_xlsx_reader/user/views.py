from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def register(request):
    if(request.method == "POST"):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f"Cuenta creada {username}!")
            return redirect("/login/")
        else:
            context = {"form": form}
            return render(request, 'register.html', context)
    else:
        form = RegisterForm()
    context = {"form": form}
    return render(request, 'register.html', context)


def login_view(request):
    print(request.method)
    if (request.method == "GET"):
        return render(request, "login.html", {})
    elif (request.method == "POST"):
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if(user):
            login(request, user)
            return redirect("/lector/dashboard/")
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
            return render(request, "login.html", {})


def logout_view(request):
    logout(request)
    return redirect("/login/")
