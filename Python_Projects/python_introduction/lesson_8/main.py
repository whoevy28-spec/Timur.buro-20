from random import choice
from string import printable, whitespace


symbols_list = list(printable.strip(whitespace))
status = False
pass_len = int(input("Из скольки символов будет состоять пароль? "))

while pass_len < 7 or pass_len > 20:
    if pass_len < 7 or pass_len > 20:
        print("Длина пароля не может быть меньше 7 или больше 20")
    pass_len = int(input("Из скольки символов будет состоять пароль? "))


while not status:
    password = "".join([choice(symbols_list) for num in range(pass_len)])
    print(f"Случайно сгенерированный пароль: {password}")    
    like = input("Вам понравился пароль? (да/нет) ").lower()
    if like == "да":
        status = True
        print(f"Отлично! Ваш новый пароль: {password}")
    elif like == "нет":
        print("Делаем новый пароль:")