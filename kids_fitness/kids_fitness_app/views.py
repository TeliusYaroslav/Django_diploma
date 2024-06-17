from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

def main(request):
    return render(request, 'kids_fitness_app/main.html')

def about_us(request):
    return render(request, 'kids_fitness_app/about_us.html')

def gallery(request):
    return render(request, 'kids_fitness_app/gallery.html')

def contacts(request):
    return render(request, 'kids_fitness_app/contacts.html')

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        username = request.POST.get('username')
        if password != password_confirm:
            messages.error(request, 'Паролі не співпадають')
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Користувач із таким email вже існує')
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Користувач із таким імям вже існує')
            return redirect('register')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        login(request, user)
        messages.success(request, 'Ви успішно зареєстровані та увійшли до системи!')
        return redirect('main')
    return render(request, 'kids_fitness_app/register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Ви успішно увійшли до системи!')
            return redirect('main')
        else:
            messages.error(request, 'Неправильне імя користувача або пароль')
    return render(request, 'kids_fitness_app/login.html')

def user_logout(request):
    logout(request)
    messages.info(request, 'Ви успішно вийшли із системи')
    return redirect('main')
