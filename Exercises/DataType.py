# int type data
number1 = 420
print(type(number1))            # type function tells the type of the values

# float type data
number2 = 40.2
print(type(number2))

# complex type data
number3 = 20j           # j is used as complex number instead of i,which is normally used in maths
print(type(number3))

# str type data
MyName = "Anusuya"
print(MyName)


name = "Anusuya"

Surname = "Das"
print(name + Surname)       # '+' connects 2 string values together


Name = "Anusuya"
print("My name is" + ' ' + Name)        # empty string is used to keep space in between is and Name

# bool type data
a = True                        # python is case-sensitive so it takes True instead of true
print(type(a))


x = 8
y = 10
print(x > y)
print(x < y)

# Binary type data: bytes

list1 = [1,2,3,121,255]              # bytes range is (0, 256), using any number over the range will give error

b = bytes(list1)                # list of byte class can't be changed as it is immutable
print(type(b))

# Binary type data: byteArray

list2 = [1,2,3,121,255]

b1 = bytearray(list2)

b1[1] = 100             # Only byteArray is mutable
print(b1[1])            # We have changed index 1 or the 2nd element of the list

# None type data

x = None
print(type(x))

# list type data

li = ["Anu","Sam","Nav","Shuv"]

print(li)
print(type(li))


li1 = ["Anu","Sam","Nav"]           # list is mutable

li1[0] = "Anusuya"
print(li1)

# tuple type data

tup = (5,10,15,20,25)
print(type(tup))            # tuple is immutable

# range type data

r = range(6)

for i in r:
    print(i)            # if r is written instead of i, it will only print range(0,6) 6 times

