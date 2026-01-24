from random import randint

count = 0

for attemp in range(10):
    if count == 3:
        break
    player = int(input("Сделайте ход - 1-камень, 2-ножницы, 3-бумага: "))
    if player == 1:
        print("Ваш ход: камень")
    elif player == 2:
        print("Ваш ход: ножницы")
    elif player == 3:
        print("Ваш ход: бумага")
    else:
        print("Неизвестный ход")

    comp = randint(1, 3)
    if comp == 1:
        print("Ход компьютера: камень")
    elif comp == 2:
        print("Ход компьютера: ножницы")
    else:
        print("Ход компьютера: бумага")

    if player == comp:
        print("Ничья!")
    elif player == 1 and comp == 2 or \
        player == 2 and comp == 3 or \
        player == 3 and comp == 1:
        count += 1
        print("Вы выиграли")
    else:
        print("Компьютер выиграл")
    
    print(f"Мои победы: {count}")