numbers_count = int(input("Сколько чисел? "))
numbers = []
for iteration in range(numbers_count):
    numbers.append(int(input(f"Число {iteration + 1}: ")))
print(numbers)