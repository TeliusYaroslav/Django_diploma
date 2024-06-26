# Дитяча фітнес студія Kids Fitness
#### Сайт створенний для швидкого та простого запису на заняття до дитячої фітнесс студії
![](readme_img/Group%2026%20(1).png)
# Зміст
#### [Учасники команди / team members](#title1)
#### [Переваги](#title5)
#### [Технології / Technologie](#title2)
#### [Використання / launch of the project](#title3)
#### [Основні Функції / main functions](#title4)


## <a id="title1">Учасники команди / team members</a>
- Ярослав Теліус / Yaroslav Telius 
>- [Github](https://github.com/TeliusYaroslav "Github")
>- [Figma](https://www.figma.com/design/B4FPYXDBsxMPMCjVxroGOU/Untitled?node-id=0-1&t=M1SHABTPBk7JIkpU-0 "Figma")
>- [Figjam](https://www.figma.com/board/SdWArB2QfOjYUKFSFBrJoM/Untitled?node-id=0-1&t=RFILsCbM5wzPIvhM-0 "Figjam")

- Ярослав Пройдисвіт / Yaroslav Proidysvit 
>- [Github](https://github.com/geniyhub "Github")
>- [Figma](https://www.figma.com/design/B4FPYXDBsxMPMCjVxroGOU/Untitled?node-id=0-1&t=szvfV9d10XQNp5V6-1 "Figma")
>- [Figjam](https://www.figma.com/board/SdWArB2QfOjYUKFSFBrJoM/Untitled?node-id=0-1&t=SHinTeKmjVd3m2uz-1 "Figjam")

- Іван Кратенко / Ivan Kratenko 
>- [Github](https://github.com/ruopodfg "Github")
>- [Figma](https://www.figma.com/design/B4FPYXDBsxMPMCjVxroGOU/Untitled?node-id=0-1&t=9pMWxwRTPLGG3xZW-1 "Figma")
>- [Figjam](https://www.figma.com/board/SdWArB2QfOjYUKFSFBrJoM/Untitled?node-id=0-1&t=ok4nPbWmv5KGHww2-1 "Figjam")

- Ілля Булкін / Ilia Bulkin
>- [Github](https://github.com/IliaBulkin "Github")
>- [Figma](https://www.figma.com/design/6w1t0BhnualqM0xpowc2F7/Untitled-(Copy)?t=J5kjRN5uvvqwk8qT-1 "Figma")
>- [Figjam](https://www.figma.com/board/dbu0I6zzVvfbtMzvg6TiIE/Untitled-(Copy)?node-id=7-361&t=chMWSF2sfJdf2S2m-1 "Figjam")

- Діана Панасенко /Panasenko Diana
>- [Github](https://github.com/PanasenkoDiana "Github")
> - [Figma](https://www.figma.com/design/B4FPYXDBsxMPMCjVxroGOU/Untitled?t=Xzdp1BLUnI5nLwLm-0 "Figma")
> - [Figjam](https://www.figma.com/board/SdWArB2QfOjYUKFSFBrJoM/Untitled?node-id=0-1&t=Y9qskt3i5QIP55ed-0 "Figjam")

## <a id="title5">Переваги </a>

###### Наш проект в першу чергу це зручна платформа для простого та швидкого запису дітей у дитячий фітнес центр.  для нас як для розробників цей проект це серйозна практика щодо створення повноцінного сайту для замовника,


## <a id="title2">Технології / Technologies</a>
- **Html**
- **JavaScript**
- **Css**
- **Python Django** 
- **SQlite3**
- **MySQL**
- **Bootstrap 5**
- **ChatGpt 3**
- **ajax**
- **jquery**
- **Git**
## <a id="title3">Використання / launch of the project</a>
### 1.Встановити додатки 
- Python django використовуємий у проекті фреймворк 
> Відкрийте консоль у вашому редакторі кода та впишіть команду 
> ```pip install django```    
>Далі перевірте чи встановился фреймворк
>```django-admin --version```
- Також проект використовує такі стандартні мови як HTML,CSS,JS Які встановлювати не потрібно
### 2. Запуск проекту(локально)
- Клонуємо проект з github-у використовуючи команду 
> git clone https://github.com/TeliusYaroslav/Django_diploma.git

## <a id="title4">Основні Функції / main functions</a>
#### views.py
- **Функція відправлення запису на заняття**
```python
# Визначаємо функцію submit_registration, яка приймає HTTP-запит як аргумент
def submit_registration(request):
    # Перевіряємо, чи метод запиту є POST
    if request.method == 'POST':
        # Отримуємо повне ім'я з POST-даних
        full_name = request.POST.get('full_name')
        # Отримуємо номер телефону з POST-даних
        phone_number = request.POST.get('phone_number')
        # Отримуємо вік дитини з POST-даних
        child_age = request.POST.get('child_age')
        # Отримуємо дату тренування з POST-даних
        training_date = request.POST.get('training_date')
        # Отримуємо email з POST-даних
        email = request.POST.get('email')
        # Тема електронного листа
        subject = 'Новий запис на заняття'
        # Тіло електронного листа
        message = f'Ім`я: {full_name}\nНомер телефону: {phone_number}\nВік дитини: {child_age}\nДата тренування: {training_date}\nEmail: {email}'
        from_email = settings.EMAIL_HOST_USER  # Вказуємо електронну адресу відправника
        to_email = [settings.EMAIL_HOST_USER]  # Вказуємо електронну адресу одержувача
        # Пробуємо виконати наступний код
        try:
            # Створюємо об'єкт EmailMessage
            email = EmailMessage(subject, message, from_email, to_email) 
            # Відправляємо електронний лист
            email.send()
            # Відображаємо сторінку реєстрації
            return render(request, 'kids_fitness_app/sign_up.html')
        # Обробляємо виключення, якщо виникла помилка
        except Exception as e:  
            # Повертаємо повідомлення про помилку
            return HttpResponse("Помилка, спробуйте знову.", status=500)  
    # Якщо метод запиту не POST
    else: 
        # Повертаємо повідомлення про недозволений метод 
        return HttpResponse("Метод не дозволен", status=405)
```

- **Функція відображення головної сторінки**
```python
def main(request):
    return render(request, 'kids_fitness_app/main.html')
```
- **Функція відображення сторінки послуг**
```python
def service(request):
    return render(request, 'kids_fitness_app/service.html')
```
- **Функція відображення сторінки запису**
```python
def sign_up(request):
    return render(request, 'kids_fitness_app/sign_up.html')
```
- **Функція відображення сторінки з інформацією про фітнес-клуб**
```python
def about_us(request):
    return render(request, 'kids_fitness_app/about_us.html')
```
- **Функція відображення галереї**
```python
def gallery(request):
    return render(request, 'kids_fitness_app/gallery.html')
```
- **Функція відображення контактів**
```python
def contacts(request):
    return render(request, 'kids_fitness_app/contacts.html')
```
- **Функція відображення сторінки реєстрації та логіка роботи**
```python
# Визначаємо функцію register, яка приймає HTTP-запит як аргумент
def register(request): 
    # Перевіряємо, чи метод запиту є POST
    if request.method == 'POST':  
        # Отримуємо email з POST-даних
        email = request.POST.get('email')
        # Отримуємо пароль з POST-даних
        password = request.POST.get('password')
        # Отримуємо підтвердження пароля з POST-даних
        password_confirm = request.POST.get('password_confirm')
        # Отримуємо ім'я користувача з POST-даних
        username = request.POST.get('username')
        # Перевіряємо, чи паролі співпадають
        if password != password_confirm:
            # Виводимо повідомлення про помилку
            messages.error(request, 'Паролі не співпадають')
            # Перенаправляємо користувача на сторінку реєстрації
            return redirect('register')
        # Перевіряємо, чи існує користувач з таким email
        if User.objects.filter(email=email).exists():
            # Виводимо повідомлення про помилку
            messages.error(request, 'Користувач із таким email вже існує')
            # Перенаправляємо користувача на сторінку реєстрації
            return redirect('register')
        # Перевіряємо, чи існує користувач з таким ім'ям
        if User.objects.filter(username=username).exists():
            # Виводимо повідомлення про помилку
            messages.error(request, 'Користувач із таким імям вже існує')
            # Перенаправляємо користувача на сторінку реєстрації
            return redirect('register')
        # Створюємо нового користувача    
        user = User.objects.create_user(username=username, email=email, password=password)
        # Зберігаємо користувача в базі даних
        user.save()
        # Виконуємо вхід користувача в систему
        login(request, user)
        # Виводимо повідомлення про успішну реєстрацію
        messages.success(request, 'Ви успішно зареєстровані та увійшли до системи!')
        # Перенаправляємо користувача на головну сторінку
        return redirect('main')
    # Відображаємо сторінку реєстрації    
    return render(request, 'kids_fitness_app/register.html')

```
- **Функція відображення логіну та логіка роботи**
```python
# Визначаємо функцію user_login, яка приймає HTTP-запит як аргумент
def user_login(request):
    # Перевіряємо, чи метод запиту є POST
    if request.method == 'POST':
        # Отримуємо ім'я користувача з POST-даних
        username = request.POST.get('username')
        # Отримуємо пароль з POST-даних
        password = request.POST.get('password')
        # Аутентифікуємо користувача
        user = authenticate(request, username=username, password=password)
        # Перевіряємо, чи користувач існує
        if user is not None:
            # Виконуємо вхід користувача в систему 
            login(request, user)
            # Виводимо повідомлення про успішний вхід
            messages.success(request, 'Ви успішно увійшли до системи!')
            # Перенаправляємо користувача на головну сторінку
            return redirect('main')
        # Якщо користувач не знайдений    
        else:
            # Виводимо повідомлення про помилку
            messages.error(request, 'Неправильне імя користувача або пароль')
    # Відображаємо сторінку входу        
    return render(request, 'kids_fitness_app/login.html')
```
- **Функція вихіду з аккаунту**
```python
    # Визначаємо функцію user_logout, яка приймає HTTP-запит як аргумент
    def user_logout(request):
        # Виконуємо вихід користувача з системи
        logout(request)
        # Виводимо повідомлення про успішний вихід
        messages.info(request, 'Ви успішно вийшли із системи')
        # Перенаправляємо користувача на головну сторінку
        return redirect('main')
```