list1 = [1, 2, 3]


def modify(k):
    k.append(10)
    print("k = ", k)


print("List1 = ", list1)
modify(list1)
print("List1 = ", list1)
