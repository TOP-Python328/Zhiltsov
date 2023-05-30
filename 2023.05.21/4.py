number = int(input("Введите 3-х значное число: "))

digit_sum = number // 100 + (number % 100) // 10 + number % 10

digit_product = (number // 100) * ((number % 100) // 10) * (number % 10)

print(f"Сумма цифр = {digit_sum}")
print(f"Произведение цифр = {digit_product}")


                #Введите 3-х значное число: 455
                #Сумма цифр = 14
                #Произведение цифр = 100