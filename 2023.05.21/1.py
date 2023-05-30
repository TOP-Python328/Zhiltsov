import datetime

# Запрос данных
first_name = input("Введите имя: ")
last_name = input("Введите фамилию: ")
birth_year = int(input("Введите год рождения: "))

# Вычисление возраста
current_year = datetime.datetime.now().year
age = current_year - birth_year

# Вывод
print(last_name, first_name,",", age)


# Введите имя: Александр
# Введите фамилию: Жильцов
# Введите год рождения: 1984
# Жильцов Александр , 39
