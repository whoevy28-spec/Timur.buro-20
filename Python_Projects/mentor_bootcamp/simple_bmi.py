weight = float(input("Ваш вес: "))
height = float(input("Ваш рост: "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    category = "Недостаточная масса тела"
elif bmi >= 18.5 and bmi <= 24.9:
    category = "Норма"
elif bmi >= 25 and bmi <= 29.9:
    category = "Избыточная масса тела"
else:
    category = "Ожирение"
print(f"Ваш BMI: {bmi:.2f} - Категория: {category}")