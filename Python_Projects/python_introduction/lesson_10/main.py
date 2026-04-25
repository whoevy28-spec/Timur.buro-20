win_state = False
playing_field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 0
all_win_coords = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7), (1, 4, 7), (2, 5, 8), (3, 6, 9))

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