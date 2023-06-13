cell1 = input()
cell2 = input()

color1 = (ord(cell1[0]) - ord('a') + int(cell1[1])) % 2
color2 = (ord(cell2[0]) - ord('a') + int(cell2[1])) % 2

if color1 == color2:
    print("да")
else:
    print("нет")

# a1
# b4
# да

# a3
# c4
# нет