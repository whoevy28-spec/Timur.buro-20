# username = "Igor"
# print("Hello", username, "im glad to see u")
# print("Hello ", username, " im glad to see u", sep="")
# print(f"Hello {username} im glad to see u")
# print()
# i = 10
# print(f"{i} {id(i)}")
# for i in range(5):
#     input()
#     print(f"Сейчас выполняются действия для i = {i} из диапозона {range(5)}")
#     print(i * 2)
#     print(f"{i} {id(i)}")

# print(f"{i} {id(i)}")
# i = 10
# print(f"{i} {id(i)}")
# words = "Видео опубликовано только для подписчиков этого телеграмм канала. Если вам понравился подобный формат, дайте знать следующей реакцией".split()
# print(words, type(words))
# for word in words:
#     print(word.strip(".,").lower())

# a = 2
# for i in range(10):
#     a *= 2
#     print(a)

# fruits = ["orange", "apple", "pineapple"]
# print("orange" in fruits)
# print("garlic" in fruits)

# letter = "banana"
# print(letter)
# fruit = "apple"
# for letter in fruits:
#     print(letter)
#     print(letter * 2)
# print("Цикл закончился")

# если в слове есть "и" заменяем на знак процента, если есть "ё" заменяем на #, иначе выводим саму букву
# word = "иваси"
# for letter in word:
#     if letter == "и":
#         print("%", end="")
#     elif letter == "ё":
#         print("#", end="")
#     else:
#         print(letter, end="")

# count = 0
# for i in range(10):
#     print("-" * 30)
#     for i in range(10):
#         count += 1
#         print(count)

# pupils = ["Катя", "Вася", "Маша"]
# grades = [5, 5, 3]

# for pupil in pupils:
#     print(pupil)

# for num in range(len(grades)):
#     print(grades[num])

# for num, pupil in enumerate(pupils):
#     print(pupil, grades[num])

double = ""
for symbol in "Привет":
    double += symbol * 2
    double = double + symbol * 2
print(double)

double = [symbol * 2 for symbol in "Привет"]
print(double)

double = "".join([symbol * 2 for symbol in "Привет"])
print(double)


squares_1 = []
for x in range(10):
    squares_1.append(x ** 3)
print(squares_1)

squares_2 = "".join([str(x ** 3) for x in range(10)])
print(squares_2)


odds_1 = []
for x in range(10):
    if x % 2 !=0:
        odds_1.append(x)
print(odds_1)

odds_2 = [x for x in range(10) if x % 2 != 0]
print(odds_2)


signal = False
if signal:
    color = "green"
else:
    color = "red"

color = "green" if signal else "red"
print(color)