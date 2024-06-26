# Дитяча фітнес студія Kids Fitness
#### Сайт створенний для швидкого та простого запису на заняття до дитячої фітнесс студії
![](readme_img/Group%2026%20(1).png)
## Учасники команди / team members

- Ярослав Теліус / Yaroslav Telius 
>[Github](https://github.com/TeliusYaroslav "Github")
[Figma](https://www.figma.com/design/B4FPYXDBsxMPMCjVxroGOU/Untitled?node-id=0-1&t=M1SHABTPBk7JIkpU-0 "Figma")
[Figjam](https://www.figma.com/board/SdWArB2QfOjYUKFSFBrJoM/Untitled?node-id=0-1&t=RFILsCbM5wzPIvhM-0 "Figjam")

- Ярослав Пройдисвіт / Yaroslav Proidysvit 
>[Github](https://github.com/geniyhub "Github")
[Figma](https://www.figma.com/design/B4FPYXDBsxMPMCjVxroGOU/Untitled?node-id=0-1&t=szvfV9d10XQNp5V6-1 "Figma")
[Figjam](https://www.figma.com/board/SdWArB2QfOjYUKFSFBrJoM/Untitled?node-id=0-1&t=SHinTeKmjVd3m2uz-1 "Figjam")

- Іван Кратенко / Ivan Kratenko 
>[Github](https://github.com/ruopodfg "Github")
[Figma](https://www.figma.com/design/B4FPYXDBsxMPMCjVxroGOU/Untitled?node-id=0-1&t=9pMWxwRTPLGG3xZW-1 "Figma")
[Figjam](https://www.figma.com/board/SdWArB2QfOjYUKFSFBrJoM/Untitled?node-id=0-1&t=ok4nPbWmv5KGHww2-1 "Figjam")

- Ілля Булкін / Ilia Bulkin
>[Github](https://github.com/IliaBulkin "Github")
[Figma](https://www.figma.com/design/6w1t0BhnualqM0xpowc2F7/Untitled-(Copy)?t=J5kjRN5uvvqwk8qT-1 "Figma")
[Figjam](https://www.figma.com/board/dbu0I6zzVvfbtMzvg6TiIE/Untitled-(Copy)?node-id=7-361&t=chMWSF2sfJdf2S2m-1 "Figjam")

- Діана Панасенко /Panasenko Diana
>[Github](https://github.com/PanasenkoDiana "Github")
[Figma](https://www.figma.com/design/B4FPYXDBsxMPMCjVxroGOU/Untitled?t=Xzdp1BLUnI5nLwLm-0 "Figma")
[Figjam](https://www.figma.com/board/SdWArB2QfOjYUKFSFBrJoM/Untitled?node-id=0-1&t=Y9qskt3i5QIP55ed-0 "Figjam")

### Технології / Technologies
- Html
- JavaScript
- Css
- Python Django 
- SQlite3
- MySQL
- Bootstrap 5
- ChatGpt 3
- ajax 
- jquery
- Git

### Запуск проекту / launch of the project 
- ---

## Основні Функції / main functions
#### views.py
- **Функція відправлення запису на заняття**
```python
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
```

- **Функція відображення головної сторінки**
- def main(request):
    return render(request, 'kids_fitness_app/main.html')

- **Функція відображення сторінки послуг**
- ``def service(request):``


- **Функція відображення сторінки запису**
- ``def sign_up(request):``
- **Функція відображення сторінки з інформацією про фітнес-клуб**
- ``def about_us(request):``
- **Функція відображення галереї**
- ``def gallery(request):``
- **Функція відображення контактів**
- ``def contacts(request):``
- **Функція відображення сторінки реєстрації та логіка роботи**
- ``def register(request):``
- **Функція відображення логіну та логіка роботи**
- ``def user_login(request):``
- **Функція вихіду з аккаунту**
- ``def user_logout(request):``







