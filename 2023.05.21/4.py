number = int(input("Введите 3-х значное число: "))

digit_sum = number // 100 + (number % 100) // 10 + number % 10
# ИСПРАВИТЬ: а вот здесь неоптимально: повторяете одни и те же операции несколько раз, когда лучше бы именно вычисленные цифры сохранить в переменные — а сами переменные digit_sum и digit_product используются только по разу, поэтому не нужны
digit_product = (number // 100) * ((number % 100) // 10) * (number % 10)

print(f"Сумма цифр = {digit_sum}")
print(f"Произведение цифр = {digit_product}")


# Введите 3-х значное число: 455
# Сумма цифр = 14
# Произведение цифр = 100


# ИТОГ: хорошо, немного доработать — 3/4