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
word = "иваси"
for letter in word:
    if letter == "и":
        print("%", end="")
    elif letter == "ё":
        print("#", end="")
    else:
        print(letter, end="")