cell1 = input()
cell2 = input()

diff_x = abs(ord(cell1[0]) - ord(cell2[0]))
diff_y = abs(int(cell1[1]) - int(cell2[1]))

if diff_x <= 1 and diff_y <= 1:
    print("да")
else:
    print("нет")

# a4
# f4
# нет

# b3
# a2
# да

# f3
# e7
# нет