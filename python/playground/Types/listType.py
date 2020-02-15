number = [1,2,3,4,5,6,7,8,9,10]
print(number)
print(number[6])

mixed = ["apple","orange","grapes","watermelon"]
print(mixed)
mixed[1] = 0x55
print(mixed)
mixed[2] = 10
print(mixed)
mixed.append(True)
print(mixed)
mixed.append(0b100010)
print(mixed)
mixed.append("characters")
print(mixed)

ok = list("characters")
print(ok)

ok1 = list(mixed)
ok1.append(ok)
print(ok1)