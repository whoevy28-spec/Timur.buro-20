win_state = False
playing_field = list(range(1, 10))
counter = 0
all_win_coords = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7), (1, 4, 7), (2, 5, 8), (3, 6, 9))

while not win_state:
    if counter % 2 == 0:
        player = "0"
    else:
        player = "X"
    print(f"Ход игрока {player}:")

    for num in range(0, 7, 3):
        print(f"|{playing_field[num]}|{playing_field[num + 1]}|{playing_field[num + 2]}|")

    position = int(input("Введите номер клетки для хода: "))
    if playing_field[position - 1] == position:
        playing_field[position - 1] = player
        counter += 1
    else:
        print("Клетка занята!")

    if counter >= 4:
        for coord_one, coord_two, coord_three in all_win_coords:
            if playing_field[coord_one - 1] == playing_field[coord_two - 1] == playing_field[coord_three - 1]:
                win_state = True
                print(f"Выиграл {player}!")

    if counter >= 9 and not win_state:
        print("Ничья...")
        win_state = True