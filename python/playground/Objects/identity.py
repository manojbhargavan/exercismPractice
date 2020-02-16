
a = 10
print(id(a))
b = 11
b = a + 10
print(id(b))
print(a == b - 10)
print(a is b)
b = a
print(id(a))
print(id(b))
print(a == b)
print(a is b)
c = 10
print(id(a))
print(id(b))
print(id(c))


l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(id(l1))
print(id(l2))
print(l1 == l2)
print(l1 is l2)
l2 = l1
print(id(l1))
print(id(l2))
print(l1 == l2)
print(l1 is l2)
