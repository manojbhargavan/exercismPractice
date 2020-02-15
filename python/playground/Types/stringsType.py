#Simple string with a double quote
simpleString1 = "this is a simple string"
print(simpleString1)

#Simple string with a single quote
simpleString2 = 'this is another simple string'
print(simpleString2)

#Multi line string can be created enclosing the string in """
multiLineString1 = """this is a 
multiline string
    hope thats fine"""
print(multiLineString1)

#Multi line string can be created escape sequence
multiLineString2 = """this is a \nmultiline string\n    hope thats fine"""
print(multiLineString2)

#Multi line string mix and match
multiLineString1 = """this is a \nmultiline string
\thope thats fine\n"""
print(multiLineString1)

#Raw string
rawString = r'C:\windows\jaffa'
print(rawString)

#Functions
capital = "delhi"
print(capital.capitalize())
print(capital.upper())
print(capital[4].upper())
print(len(capital))

#Constructor 
simpleString3 = str(0b1010)
print(simpleString3)
simpleString3 = str(0x898898ABC)
print(simpleString3)