# Напишіть функцію визначення кількості днів у конкретному місяці.
# Ваша функція повинна приймати два параметри: month - номер місяця у вигляді
# цілого числа в діапазоні від 1 до 12 і year - рік, що складається із чотирьох цифр.
# Перевірте, чи функція коректно обробляє місяць лютий високосного року.
from datetime import date


def get_days_in_month(month, year):
    day1 = date(year=year, month=month, day=1)
    day2 = date(year=year + 1, month=1, day=1) if month == 12 else date(year=year, month=month + 1, day=1)
    return (day2 - day1).days