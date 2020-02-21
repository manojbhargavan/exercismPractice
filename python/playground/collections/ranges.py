# range(stop)
# range(start, stop)
# range(start, stop, step)
for i in range(3):
    print(i)
print()
for i in range(1, 3):
    print(i)
print()
for i in range(2, 11, 2):
    print(i)

listItems = ["Apple", "Orange", "Powder", "Soap", "Paste"]

for index, item in enumerate(listItems):
    print(item, index)
