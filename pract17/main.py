from calendar_tools import UkrainianCalendar
from math_utils import Calculator
from text_analysis import TextStats
from datetime import datetime

def menu():
    print("1. Переглянути державні свята")
    print("2. Перевірити, чи робочий день")
    print("3. Калькулятор")
    print("4. Аналіз тексту")
    print("0. Вийти")

calendar = UkrainianCalendar()
calc = Calculator()

while True:
    menu()
    choice = input("Оберіть пункт меню: ")
    if choice == "1":
        holidays = calendar.get_holiday_list()
        print("Державні свята України:")
        for h in holidays:
            print("-", h)
    elif choice == "2":
        date_str = input("Введіть дату у форматі РРРР-ММ-ДД: ")
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
            is_work = calendar.is_working_day(date)
            print("Робочий день." if is_work else "Вихідний або свято.")
        except:
            print("Невірний формат дати.")
    elif choice == "3":
        print("Калькулятор:")
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
        print("Операції: +, -, *, /")
        op = input("Оберіть операцію: ")
        if op == "+":
            print("Результат:", calc.add(a, b))
        elif op == "-":
            print("Результат:", calc.subtract(a, b))
        elif op == "*":
            print("Результат:", calc.multiply(a, b))
        elif op == "/":
            print("Результат:", calc.divide(a, b))
        else:
            print("Невідома операція.")
    elif choice == "4":
        text = input("Введіть текст для аналізу: ")
        stats = TextStats(text)
        print("Кількість слів:", stats.count_words())
        most_common = stats.most_common_letter()
        if most_common:
            print(f"Найчастіша літера: '{most_common[0]}' ({most_common[1]} разів)")
        else:
            print("В тексті немає літер.")
    elif choice == "0":
        print("Вихід з програми.")
        break
    else:
        print("Невірний вибір.")
