from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse


def submit_registration(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        child_age = request.POST.get('child_age')
        training_date = request.POST.get('training_date')
        email = request.POST.get('email')

        subject = 'Новий запис на заняття'
        message = f'Ім`я: {full_name}\nНомер телефону: {phone_number}\nВік дитини: {child_age}\nДата тренування: {training_date}\nEmail: {email}'
        from_email = settings.EMAIL_HOST_USER
        to_email = [settings.EMAIL_HOST_USER]

        try:
            email = EmailMessage(subject, message, from_email, to_email)
            email.send()
            return render(request, 'kids_fitness_app/sign_up.html')
        except Exception as e:
            return HttpResponse("Помилка, спробуйте знову.", status=500)

    else:
        return HttpResponse("Метод не дозволен", status=405)

def send_mails(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        user_email = request.POST.get('email')
        email = EmailMessage(
            subject='Питання від користувача',
            body=text,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            headers={'Reply-To': user_email}
        )
        email.send(fail_silently=False)
        return render(request, 'kids_fitness_app/main.html')
    else:
        return HttpResponse("Method not allowed", status=405)

def main(request):
    return render(request, 'kids_fitness_app/main.html')

def service(request):
    return render(request, 'kids_fitness_app/service.html')

def sign_up(request):
    return render(request, 'kids_fitness_app/sign_up.html')

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
