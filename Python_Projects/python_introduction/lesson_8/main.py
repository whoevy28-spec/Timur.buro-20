from random import choice
from string import printable, whitespace


symbols_list = list(printable.strip(whitespace))
status = False
password_lenght = 0

while password_lenght < 7 or password_lenght > 20:
    password_lenght = int(input("Из скольки символов будет состоять пароль? "))
    if password_lenght < 7 or password_lenght > 20:
        print("Длина пароля не может быть меньше 7 или больше 20")

while not status:
    password = ""
    for num in range(password_lenght):
        password += choice(symbols_list)   
    print(f"Случайно сгенерированный пароль: {password}")    
    like = input("Вам понравился пароль? (да/нет) ").lower()
    if like == "да":
        status = True
        print(f"Отлично! Ваш новый пароль: {password}")
    elif like == "нет":
        print("Делаем новый пароль:")