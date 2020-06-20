"""Сделал 2 варианта решения не уверен какой боле коркетнный в плане написания кода"""


def analitic(**kwargs):
    return kwargs


print(analitic(name=input('Имя:'), surname=input('Фамилия:'), birhday_date=input('Дата рождения:'),
               city_name=input('Городпроживания:'), email=input('Email:'), phone_number=input('Номер телефона:')))

name = input('Имя:')
surname = input('Фамилия:')
birthday_date = input('Дата рождения:')
city = input('Городпроживания:')
email = input('Email:')
phone_number = input('Номер телефона:')

print(analitic(name=name, surname=surname, birhday_date=birthday_date,
               city_name=city, email=email, phone_number=phone_number))
