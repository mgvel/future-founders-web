import os
import sys

print("Hello, world!")
print(sys.version)

x = 80
y = 8.5

z = x + y

# print("x + y = ", z)


# while x > 10:
#     print ("x =", x)
#     x = x - 10
 
c = 0

for i in range(x):
    c += 10
    x -= 10
    if c <= x:
        print(c, x)


class Calc:
    def add(x, y):
        return x + y

    def sub(x, y):
        return x - y

    def mul(x, y):
        return x * y

    def pow(x, y):
        return x ** y


def calc(x, y, op):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '**':
        return x ** y
    else:
        print("Operator not known")

x = 2
y = 3

print("x = ", x)
print("y = ", y)

# print("X + Y = ", calc(x, y, '+'))
# print("X - Y = ", calc(x, y, '-'))
# print("X * Y = ", calc(x, y, '*'))
# print("X ** Y = ", calc(x, y, '**'))


print("X + Y = ", Calc.add(x, y))
print("X - Y = ", Calc.sub(x, y))
print("X * Y = ", Calc.mul(x, y))
print("X ** Y = ", Calc.pow(x, y))

print()

l1 = [1, 2, 3, 4]

print("l1", l1)

l2 = [1, 2.0, 4, 6]

print("l2", l2)


l3 = [1, 3.0, 'x', "Python", l1]

print("l3", l3)


name = "This is quick intro to python"

for i in l1:
    print(i)

# for x in name:
#     print(x)

print(l1[0:2])

print(name[0:4])


d1 = {'a': 100, 'b': 220}

k1 = ['a', 'b', 'c', 'd', 'e']

v1 = [87, 92, 96, 108, 45.9]

print(type(d1), d1['a'])
print(d1.keys(), d1.values())

d2 = dict(zip(k1, v1))

print(d2.keys(), d2.values())
print(d2)

for xx, yy in d2.items():
    print(xx, "=>", yy)