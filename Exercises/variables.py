name = "anusuya"
number = 1234

print(name)         #prints out the string that is kept inside the variable
print(number)       #prints out the integer that is kept inside the variable
print("name")       #prints name value because it is mentioned as string not variable

x = 25
x = 50

print(x)
'''Python interpreter only takes the last value that is assigned to the variable
So that means only one value can be assigned at a time to a variable.'''

# Swapping

a = 50
b = 60

a,b = b,a

print("This value is now a =", a)
print("This value is now b =", b)