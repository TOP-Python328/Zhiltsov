num1 = int(input())
num2 = int(input())

if num1 % num2 == 0:
    print(f"{num1} делится на {num2} нацело")
    print(f"частное: {num1 // num2}")
else:
    print(f"{num1} не делится на {num2} нацело")
    print(f"неполное частное: {num1 // num2}\nостаток: {num1 % num2}")
