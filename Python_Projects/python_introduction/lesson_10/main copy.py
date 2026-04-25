win_state = False
playing_field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 0
all_win_coords = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7), (1, 4, 7), (2, 5, 8), (3, 6, 9))

    # 3 на 0, добавили запятую, написали семь, добавили запятую, написали 3
    # через попытки в лаборатории
    # Заменили константные (постоянные) числа на переменные (0 на i)
    # Изучили что и в каком виде содержит переменная i 
    # Изучили что такое range и как изменять то, что он выдает
    # Использовали конкретику и конкретизирующие (уточняющие) вопросы
    # Использовали способ сравнивания что верное, а что нет
    
while not win_state:
    if counter % 2 == 0:
        player = "0"
    else:
        player = "X"
    print(f"Ход игрока {player}:")

    for i in range(0, 7, 3):
        print(f"|{playing_field[i]}|{playing_field[i + 1]}|{playing_field[i + 2]}|")

    position = int(input("Введите номер клетки для хода: "))
    if playing_field[position - 1] == position:
        playing_field[position - 1] = player
        counter += 1
    else:
        print("Клетка занята!")

    if counter >= 4:
        for coord_1, coord_2, coord_3 in all_win_coords:
            if playing_field[coord_1 - 1] == playing_field[coord_2 - 1] == playing_field[coord_3 - 1]:
                win_state = True
                print(f"Выиграл {player}!")

    if counter >= 9 and not win_state:
        print("Ничья...")
        win_state = True

    # if playing_field[position - 1] != "X" or playing_field[position - 1] != "0":
    #     playing_field[position - 1] = player
    #     counter += 1
    # else:
    #     print("Клетка занята!")
    
    # if playing_field[position - 1] in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    #     playing_field[position - 1] = player
    #     counter += 1
    # else:
    #     print("Клетка занята!")


    # Пока кто-то не выиграет игроки ходят по очереди
    # Ходит первый игрок, ставя 0 в любую клетку
    # Ходит второй игрок, ставя X в любую клетку, кроме занятой
    # Ходит первый игрок, ставя 0 в любую клетку, кроме занятых
    # Ходит второй игрок, ставя X в любую клетку, кроме занятых
    # Ходит первый игрок, ставя 0 в любую клетку, кроме занятых 
    # Если первый игрок поставил 3 нуля в ряд, или по диагонали, то он выиграл и игра завершается. Если нет:
    # Ходит второй игрок, ставя X в любую клетку, кроме занятых
    # Если второй игрок поставил 3 крестика в ряд, или по диагонали, то он выиграл и игра завершается. Если нет, действия повторяются по очереди, чередуя игроков