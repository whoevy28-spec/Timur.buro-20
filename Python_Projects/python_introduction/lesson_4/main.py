original_text = input("Print message: ")
lenght_text = len(original_text)
print(f"Lenght of the text: {lenght_text}")

print(f"Last symbol is: {original_text[-1]} and second symbol: {original_text[1]}")
print(f"First three letters are: {original_text[:3]} and last three letters are: {original_text[-3:lenght_text + 1]}")

colored_text = "\u001b[31;46" + original_text + "\u001b[0m"
print(f"Painted: {colored_text}")

color_start = int(input("Which letter do you want to color the word from? "))
color_end = int(input("Which letter do you want to color the word by? "))
color_name = input("What color do you want to paint it? (Red, blue) ").lower()
if color_name == "red":
    colored_text = "\u001b[31m" + original_text[color_start - 1:color_end] + "\u001b[0m"
elif color_name == "blue":
    colored_text = "\u001b[34m" + original_text[color_start - 1:color_end] + "\u001b[0m"
else:
    colored_text = "\u001b[32m" + original_text[color_start - 1:color_end] + "\u001b[0m"
print(original_text[0:color_start - 1] + colored_text + original_text[color_end:])

old_char = input("What is/are letter(s) you want to change? ")
new_char = input("With which one letter you want to change letter you wrote? ")
modified_text = original_text.replace(old_char, new_char)
print(f"There is your modified text: {modified_text}")

even_chars = modified_text[::2]
odd_chars = modified_text[1::2]
print(f"There is an odd letters: {odd_chars}, and even letters: {even_chars}")

reversed_text = original_text[::-1]
print(f"There is reversed text: {reversed_text}")

middle_index = lenght_text // 2
swapped_text = original_text[middle_index:lenght_text + 1] + original_text[:middle_index]
print(f"Swapped text: {swapped_text}")