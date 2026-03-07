def calculate_bmi(weight, height):
    """Возвращает индекс массы тела по весу (кг) и росту (м)."""
    return weight / (height ** 2)

def get_bmi_category(bmi):
    """Принимает BMI, возвращает категорию (строку)."""
    if bmi < 18.5:
        return "Недостаточная масса тела"
    elif bmi < 25:  # Упрощённое условие
        return "Норма"
    elif bmi < 30:
        return "Избыточная масса тела"
    else:
        return "Ожирение"

def main():
    weight = float(input("Ваш вес: "))
    height = float(input("Ваш рост: "))
    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)
    print(f"Ваш BMI: {bmi:.2f} - Категория: {category}")

if __name__ == "__main__":
    main()