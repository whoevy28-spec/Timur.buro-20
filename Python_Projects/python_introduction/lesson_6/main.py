win = False
all_letters = []
true_letters = []
points = [0, 0, 0]
counter = 0

secret_word = input("Введите слово для игры: ").lower()
print("\033[2J")

while not win:
    letter = input(f"\nИгрок {counter + 1}, ведите букву:")

    if letter in all_letters:
        print("Буква уже была введена")
    else:
        all_letters.append(letter)    
        if letter not in secret_word:
            print("Такой буквы нету в слове")
        else:
            print("Вы угадали букву")
            true_letters.append(letter)
            points[counter] += 1

    win = True
    for letter in secret_word:
        if letter in true_letters:
            print(letter, end="")
        else:
            print("*", end="")
            win = False

    counter += 1
    if counter == 3:
        counter = 0

print(f"\nИгрок 1: {points[0]}\nИгрок 2: {points[1]}\nИгрок 3: {points[2]}\n")