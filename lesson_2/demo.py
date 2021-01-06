import math

# 1
def print_sqrt():
    i, nums, sqrts = 1, [], []
    i = int(input("Enter the number you want to get sqrt of:\n"))
    while i >= 0:
        nums.append(i)
        sqrts.append(math.sqrt(i))
        i = int(input("Enter the number you want to get sqrt of:\n"))
    return nums, sqrts

# 2
def max(n):
    num1, nums = int(input("Enter a number:\n")), []
    max = num1
    nums.append(num1)
    while n > 1:
        next_num = int(input("Enter a number:\n"))
        nums.append(next_num)
        if next_num > max:
            max = next_num
        n -= 1
    return max, nums

# 3
def mul_or_add():
    op = input("Enter an operation: ")
    ops = {"*": int.__mul__, "+": int.__add__}
    while op not in ops.keys():
        op = input("Enter * or +: ")
    n = int(input("Enter numbers amount: "))
    nums = []
    result = 1
    while n > 0:
        _n = int(input("Enter a number: "))
        nums.append(_n)
        result = ops[op](result, _n)
        n -= 1
    result = result if op == "*" else result - 1
    return op, nums, result

def f(n):
    if n < 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)

# 4
def first_n_fibonacci(n):

    fibs = []
    for i in range(1, n + 1):
        fibs.append(f(i))
    return fibs

# 5
def fibs_smaller_than_(n):
    i = 1
    fibs = []
    while n > f(i):
        fibs.append(f(i))
        i += 1
    return fibs

# 6
c1 = int(input("Enter the first degrees in Celsius: "))
c2 = int(input("Enter the second degrees in Celsius: "))
for i in range(c1, c2 + 1):
    f = i * 1.8 + 32
    f = round(f, 2)
    print("C: " + str(i) + "°C" + "\t" + "F: " + str(f) + "°F")

# 7
n = int(input("Enter a number: "))
x1 = int(input("Enter x" + str(1) + ": "))
y1 = int(input("Enter y" + str(1) + ": "))
x0, y0 = x1, y1
p = 0
for i in range(1, n):
    x_1 = int(input("Enter x" + str(i + 1) + ": "))
    y_1 = int(input("Enter y" + str(i + 1) + ": "))
    dx, dy = x1 - x_1, y1 - y_1
    l = math.sqrt(dx ** 2 + dy ** 2)
    x1, y1 = x_1, y_1
    p += l
p += math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
print(p)


# LISTS
# 8
l = []
n = int(input("List size: "))
for i in range(n):
    l.append(int(input("Enter the list entry: ")))
mean = float(sum(l)) / max(len(l), 1)
# print(mean)
for i in l:
    print(round(i / mean, 2))

l = [z for z in range(10)] # list of 10 elements

# 9
l = []
n = int(input("List size: "))
for i in range(n):
    l.append(int(input("Enter the list entry: ")))
for i in range(1, len(l) - 1):
    e = l[i]
    if e > l[i - 1] and e > l[i + 1]:
        print(e)

# 10
l = []
n = int(input("List size: "))
for i in range(n):
    l.append(int(input("Enter the list entry: ")))
l = list(reversed(l)) # l = l[::-1]
print(l)
for i in l:
    print(i)

# 11
l = []
n = int(input("List size: "))
for i in range(n):
    l.append(int(input("Enter the list entry: ")))
len = len(l)
a, b = 1, 1
while a > 0 and b > 0:
    a, b = [int(v) for v in input("Enter 2 numbers: ").split()]
    a = min(a, len)
    b = min(b, len)
    if a <= b:
        print(l[a:b])
    else:
        print(l[b:a:-1])

# 12
l = []
n = int(input("List size: "))
for i in range(n):
    l.append(int(input("Enter the list entry: ")))
l = list(dict.fromkeys(l))
print(l)

# 13
l1 = []
n = int(input("1st list size: "))
for i in range(n):
    l1.append(int(input("Enter the 1st list entry: ")))
l2 = []
m = int(input("2d list size: "))
for i in range(n):
    l2.append(int(input("Enter the 2d list entry: ")))
l1_s = set(dict.fromkeys(l1))
l2_s = set(dict.fromkeys(l2))
print(list(l1_s.intersection(l2_s)))

# 14
class CRM(object):
    def __init__(self):
        self.names = []
        print("System has been started.")

    def find(self, name):
        return name in self.names

    def add(self, name):
        if not self.find(name):
            self.names.append(name)
            print(name + " has been added to the system.")
            return
        print(name + " is already in the system.")

    def show(self, as_list=False):
        if not as_list:
            for i in self.names:
                print(i)
        else:
            print(self.names)

    def delete(self, name):
        if self.find(name):
            self.names.remove(name)
            print(name + " has been deleted from the system.")
            return
        print(name + " is not in the system.")

    def stop(self):
        self.names = []
        print("The system has been stopped.")

crm = CRM()
crm.add("Aake")
crm.add("Menke")
crm.show()
crm.show(True)
crm.delete("Saunter")
crm.delete("Aake")
crm.show(True)
crm.stop()
crm.show(True)