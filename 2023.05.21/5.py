miles_integer, miles_fraction = int(input("")), int(input(""))
miles = float(f'{miles_integer}.{miles_fraction}')
kilometers = miles * 1.61
# КОММЕНТАРИЙ: если результат округления должен быть использован где-то ещё, тогда используете функцию round(); в данном случае выгоднее воспользоваться синтаксисом f-строк
kilometers = round(kilometers, 1)
print(f"{miles} миль = {kilometers} км")


# 65
# 6
# 65.6 миль = 105.6 км


# ИТОГ: очень хорошо — 4/5
