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
    height = float(input("Ваш рост (метры): "))
    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)

    person = {
        "weight": weight,
        "height": height,
        "bmi": bmi,
        "category": category
    }

    print(person)

if __name__ == "__main__":
    main()