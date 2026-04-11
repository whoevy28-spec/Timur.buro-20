ALPHABET_RU = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ALPHABET_EN = "abcdefghijklmnopqrstuvwxyz"


cipher = []
result = ""

message = input("Введите сообщение: ").lower()
step = int(input("Введите шаг списка: "))
lang = input("Введите язык (RU/EN): ").lower()

if lang == "ru":
    alphabet = ALPHABET_RU
elif lang == "en":
    alphabet = ALPHABET_EN

for symbol in message:
    cipher.append(alphabet.find(symbol) + step)
print(F"Шифр: {cipher}")

for num in cipher:
    result += alphabet[num - step]
print(f"Ваше слово: {result}")