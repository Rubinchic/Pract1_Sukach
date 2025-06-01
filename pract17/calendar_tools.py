from datetime import datetime

class UkrainianCalendar:
    def __init__(self):
        self.holidays = [
            ("Новий рік", "01-01"),
            ("Різдво Христове", "07-01"),
            ("Міжнародний жіночий день", "08-03"),
            ("Великдень", ""),  # Дата змінна
            ("День праці", "01-05"),
            ("День перемоги над нацизмом", "09-05"),
            ("День Конституції України", "28-06"),
            ("День незалежності України", "24-08"),
            ("День захисників і захисниць України", "14-10"),
            ("Різдво Христове (григоріанський календар)", "25-12"),
        ]
        self.fixed_holidays = [h[1] for h in self.holidays if h[1]]

    def get_holiday_list(self):
        return [name for name, _ in self.holidays]

    def is_working_day(self, date: datetime):
        date_str = date.strftime("%d-%m")
        # Вихідні — субота, неділя або офіційне свято
        if date.weekday() in [5, 6]:
            return False
        if date_str in self.fixed_holidays:
            return False
        return True
