# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30
ML_PER_L = 1000


# На все расчеты делаю отдельные функции
def calculation_bmi(weight, height) -> float:
    """Расчет индекса массы тела"""
    return round(weight / (height ** 2), 1)


def calculation_water_needed(weight) -> float:
    """Расчет необходимой воды на массу тела в литрах"""
    water_ml = weight * WATER_PER_KG
    return round(water_ml / ML_PER_L, 1)


# 1. Знакомство
user_name = input("Введите имя: ")
user_name = user_name.strip()
user_name = user_name.title()

user_age = input(f"Привет, {user_name}! Укажи свой возраст: ")
# Пробуем получить число до тех пор пока пользователь не введет корректно
while True:
    user_age = user_age.strip()
    try:
        user_age = int(user_age)
        break
    except ValueError:
        user_age = input("Пожалуйста укажи возраст числом (например 25): ")

# 2. Сбор данных
user_weight = input("Укажи свой вес: ")
while True:
    user_weight = user_weight.strip()
    try:
        user_weight = float(user_weight)
        break
    except ValueError:
        user_weight = input("Пожалуйста укажи вес числом (например 61.5): ")


user_height = input("Укажи свой рост (в метрах, например 1.70): ")
while True:
    user_height = user_height.strip()
    try:
        user_height = float(user_height)
        break
    except ValueError:
        user_height = input("Пожалуйста укажи рост числом (например 1.70): ")

# На случай если все таки укажет в сантиметрах
if user_height > 100:
    user_height /= 100

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = calculation_bmi(user_weight, user_height)

# Подсчет воды: вес * 30 мл
water_needed = calculation_water_needed(user_weight)

# Отделяем часть получения данных от расчетной части
print("\n" + "=" * 30 + "\n")

# 4. Вывод красивого результата
print(f"Отчет для пользователя: {user_name} ({user_age} г.)")
print(f"Твой Индекс Массы Тела: {bmi:.1f}")
print(f"Рекомендуемая норма воды: {water_needed:.1f} л. в день")
print("Расчет окончен. Будьте здоровы!")
