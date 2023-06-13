year = int(input())

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("да")
else:
    print("нет")

# 2010
# нет

# 1984
# да