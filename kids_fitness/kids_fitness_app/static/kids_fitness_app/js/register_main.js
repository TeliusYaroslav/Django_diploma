function validateForm() {
    var username = document.getElementById("username").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var password_confirm = document.getElementById("password_confirm").value;

    if (username.trim() == '') {
        alert('Пожалуйста, введите имя пользователя.');
        return false;
    }

    if (email.trim() == '') {
        alert('Пожалуйста, введите адрес электронной почты.');
        return false;
    }

    if (password.trim() == '') {
        alert('Пожалуйста, введите пароль.');
        return false;
    }

    if (password != password_confirm) {
        alert('Пароли не совпадают.');
        return false;
    }

    return true;
}