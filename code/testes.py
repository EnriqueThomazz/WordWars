from random import choice, choices

size = ["3", "4", "5", "6", "7", "8", "9", "10"]

dif = 50 // len(size)

for c in range(min(dif, 5)):
    size.append(choice(size[3:]))

print(size)
