import math
station = "Llanfair­pwllgwyngyll­gogery­chwyrn­drobwll­llan­tysilio­gogo­goch "
print(len(station))

print("New" + "found" + "jaffa")
s = "New"
print(id(s))
s += "found"
print(id(s))
s += "jaffa"
print(id(s))
print(s)

# join
separator = ""
strColl = ("New", "found", "jaffa")
ns = separator.join(strColl)
print(ns)

# partition
depart, sep, arrive = "Hyderabad:Kochi".partition(":")
print(depart, sep, arrive)
depart, _, arrive = "Hyderabad:Kochi".partition(":")
print(depart, arrive)

# format
print("My name is {0}, working as {1}. {0} works in {2}".format("Manoj", "Jaffa", "Gachibowli"))
print("PI= {}, e={}".format(math.pi, math.e))
print("Pi={m.pi:.3f}, e={m.e:.3f}".format(m=math))

# string interpolation
print(f"Pi={math.pi:.4f}, e={math.e:.4f}")
