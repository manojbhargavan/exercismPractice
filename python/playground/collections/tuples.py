def printEmps(empTup):
    for emp in empTup:
        length = len(str(emp[0])) + len(str(emp[1])) + len(str(emp[2])) + len(emp) * 2
        print("*" * length)
        print(emp)
        print(emp[0])
        print("*" * length)
        print()


emp1 = (10, "manoj", "cognizant")
emp2 = (20, "nandan", "pratiksha")

employees = (emp1, emp2)
printEmps(employees)
employees *= 3
printEmps(employees)
print(employees)


def minmax(items):
    return max(items), min(items)


lowest, highest = minmax([10, 20, 30, 40, 5, 50, 60, 55])
print(lowest, highest)
(a, (b, (c, d))) = (1, (2, (3, 4)))
print(a, b, c, d)

# Swap Variables
a = "peanutbutter"
b = "jelly"
c = "love"
a, b, c = c, a, b
print(a, b, c)


# Single Element Tuple
s = (10,)
print(s)
print(type(s))
e = ()
print(e)
print(type(e))
