# Завдання 1: Фільтрація чисел
# Вивести всі числа від 1 до 100, які кратні 3, але не кратні 5
filtered_numbers = [x for x in range(1, 101) if x % 3 == 0 and x % 5 != 0]
print("Завдання 1 — Числа, кратні 3, але не кратні 5:")
print(filtered_numbers,"\n")


# Завдання 2: Перетворення температури
# Перетворення температур з Цельсія у Фаренгейти
celsius = [0, 10, 20, 30, 40, 100]
fahrenheit = [c * 9 / 5 + 32 for c in celsius]
print("Завдання 2 — Температури у Фаренгейтах:")
print(fahrenheit,"\n")


# Завдання 3: Квадрати парних чисел
# Створити список квадратів парних чисел від 1 до 50
even_squares = [x ** 2 for x in range(1, 51) if x % 2 == 0]
print("Завдання 3 — Квадрати парних чисел від 1 до 50:")
print(even_squares,"\n")


# Завдання 4: Аналіз тексту
# Порахувати довжини кожного слова у рядку
text = "Python is amazing and powerful language"
word_lengths = [len(word) for word in text.split()]
print("Завдання 4 — Довжини слів у тексті:")
print(word_lengths,"\n")


# Завдання 5: Складні числа
# Складне число — не просте
composite_numbers = [
    x for x in range(2, 101)
    if len([d for d in range(1, x + 1) if x % d == 0]) > 2
]
print("Завдання 5 — Складні числа від 1 до 100:")
print(composite_numbers)
