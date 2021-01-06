import lesson_4.triangle as triangle
import lesson_4.dictionary as dictionary

# 4.4
l = []
list_items_amount = int(input("Enter the list size: "))
for i in range(list_items_amount):
    l.append(input("Enter the values: "))
counter_dictionary = {}
for i in range(list_items_amount):
    if l[i] not in counter_dictionary:
        counter_dictionary[l[i]] = 1
    else:
        counter_dictionary[l[i]] += 1

for key, value in counter_dictionary.items():
    print(f"List contains {value} '{key}'s.")

# 4.5
d = {}
while True:
    command = (input("Enter the command: ")).lower()
    if command == "insert":
        name = input("Enter the name: ")
        number = input("Enter the number: ")
        if name not in d:
            d[name] = number
        elif name in d:
            print("The contact already exists.")
    elif command == "get":
        name = input("Enter the name: ")
        if name not in d:
            print("404. The contact doesn't exist.")
        else:
            print(d[name])
    elif command == "delete":
        name = input("Enter the name: ")
        if name not in d:
            print("404. The contact doesn't exist.")
        else:
            d.pop(name)
    elif command == "stop":
        break
    else:
        print("There's no such a command. Please reenter the command.")

# 4.6
print("\nExtended dictionary 4.6\n")
d = dictionary.Dictionary()
while True:
    command = (input("Enter the command: ")).lower()
    if command == "insert":
        name = input("Enter the name: ")
        try:
            number = input("Enter the number: ")
            d.add(name, number)
        except ValueError as error:
            print("An error has occurred " + str(error) + ".")
            print("Recheck your data and try again.")
    elif command == "get":
        name = input("Enter the name: ")
        print(d.get(name))
    elif command == "delete":
        name = input("Enter the name: ")
        d.delete(name)
    elif command == "stop":
        break
    else:
        print("There's no such a command. Please reenter the command.")

# 4.7
t = triangle.Triangle(3, 3, 3)
print("Perimeter is " + str(t.perimeter()) + ".")
print("Area is " + str(t.area()) + ".")
t_type = t.triangle_type()
assert t_type == 'Equilateral'

t = triangle.Triangle(3, 3, 4)
print("Triangle circumscribed circle radius is " + str(t.radius_of_circumscribed_circle()) + ".")
t_type = t.triangle_type()
assert t_type == 'Isosceles'

t = triangle.Triangle(3, 4, 5)
print("Triangle inscribed circle radius is " + str(t.radius_of_inscribed_circle()) + ".")
t_type = t.triangle_type()
assert t_type == 'Versatile'
