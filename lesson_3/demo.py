a = 1 / 3
b = 0.1 / 0.3
print(a == b)
print(abs(a - b) < 1e-9)
print("{0:.55f}".format(0.1))
print("abc" < "abd")

# кортеж
values = (1, 2, 3)
print(values)

print([int(z) for z in "1 2 3".split()])

values = []

a, b = [int(v) for v in input("Enter rows and columns count:\n").split()]
for x in range(a):
    row = [int(z) for z in input().split()]
    values.append(row)

for x in range(a):
    for y in range(b):
        print(values[x][y], end=" ")
    print()

# 1
for y in range(b):
    s = 0
    for x in range(a):
        s += values[x][y]
    print(s, end=" ")

# 2
values = []
n = int(input())
for x in range(n):
    row = [0 for z in range(n)]
    values.append(row)

print(values)

for x in range(n):
        values[x][x] = 1

for x in range(n):
    for y in range(n):
        print(values[x][y], end=" ")
    print()

# 3
values= []
a, b = [int(v) for v in input("Enter rows and columns count:\n").split()]
for x in range(a):
    row = [int(z) for z in input().split()]
    values.append(row)

for x in range(b):
    for y in range(a):
        print(values[y][x], end=" ")
    print()
import math


def factorial(a):
    fact = 1
    for i in range(2, a + 1):
        fact *= i
    return fact

def c(n, k):
    return factorial(n)//(factorial(k) * factorial(n - k))

# 4
def sub_sq(x1, x2):
    return (x1 - x2)**2

def distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt(sub_sq(x1, x2) + sub_sq(y1, y2) + sub_sq(z1, z2))

# 5
def return_even(list):
    list2 = []
    for i in range(len(list)):
        if i % 2 == 1:
            list2.append(list[i])
    return list2

print(return_even([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# 6
def diameter(r):
    return 2 * r

def length(r):
    return 2 * math.pi * r

def square(r):
    return math.pi * r * r

# 7
def circle_info():
    r = int(input("Enter radius of the circle: "))
    print("Diameter of the circle = {}".format(diameter(r)) + " units.")
    print("Circumference of the circle = {} units".format(length(r)))
    print("Area of the circle = {} sq. units".format(square(r)))

circle_info()

8
n = sorted([int(z) for z in input().split()])
m = sorted([int(z) for z in input().split()])

print(n)
print(m)

def sort(n, m):
    for x in m:
        n.append(x)
    return sorted(n)

print(sort(n, m))

def mergesort(n ,m):
    return

# множества
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3, 4, 4} # -> {1, 2, 3, 4}
print(s1 == s2)
print(72 in s1)
print(2 in s2)

s1.add(45)
print(s1)

s1.discard(1) # в отличие от remove() не выдаёт ошибку, если элемента нет в множестве
print(s1)

for i in s1:
    print(s1)

empty_set = set()
print(empty_set)

# 4.1
l = [int(z) for z in input().split()]
print(len(dict.fromkeys(l)))

# 4.2
s = set()
while True:
    s1 = int(input())
    if s1 in s:
        print("Present")
    s.add(s1)
    if s1 == 666:
        break

# 4.3
class Addresses(object):
    def __init__(self):
        self.addresses = set()
        print("Book has been opened.")

    def find(self, address):
        return address in self.addresses

    def add(self, address):
        if not self.find(address):
            self.addresses.add(address)
            print("Address " + address + " has been added to the book.")
            return
        print(address + " is already in the book.")

    def delete(self, address):
        if self.find(address):
            print(address + " has been deleted from the book.")
        self.addresses.discard(address)