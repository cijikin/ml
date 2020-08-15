import math
import random
import shutil
from colorama import Style, Fore
from termcolor import colored

class Lesson1():

    def __init__(self):
        self.enter_2_nums = "Enter 2 numbers (space-separated):\n"

    tasks = {"1": "Користувач вводить ім’я. Привітайтесь з ним по імені й зі знаком оклику в кінці.",
             "2": "Задано 3 числа. Вивести їх суму.",
             "3": "Дано число. Вивести попереднє й наступне відносного нього.",
             "4": "Знайти сторону квадрата по його площі.",
             "5": "Задано 3 сторони трикутника. Знайти його периметр і площу.",
             "6": "Дано розмір кредиту й одноразові відсотки по ньому.\n"
                  "Знайти загальну суму з відсотками й розмір переплати.",
             "7": "Реалізуйте простий калькулятор, що отримує два числа й виводить результати\n"
                  "застосування стандартних математичних операцій над ними.",
             "8": "Дано два числа, що задають інтервал.\n"
                  "Згенерувати й вивести два випадкових числа у вказаному\n"
                  "інтервалі - ціле й раціональне.",
             "9": "Дано 2 числа. Вивести меньше з них.",
             "10": "Реалізувати функцію sign(x).",
             "11": "Реалізуйте ще один простий калькулятор,\n"
                   "що отримує два числа й операцію і виводить результат виконання операції\n"
                   "над введеними значеннями. Допустимі операції: + - * /",
             "12": "Дано коефіцієнти a, b, c квадратного рівняння ax^2+bx+c=0. Знайти корені рівняння.",
             "13": "Пакет мобільного зв’язку передбачає 100 хвилин і 30 смс на місяць при фіксованій абонплаті у 30 гривень.\n"
                   "Надалі дзвінки тарифікуються по 30 копійок за хвилину, а смс по 25 копійок за одиницю.\n"
                   "Дано кількість хвилин й смс по номеру за місяць. Розрахувати загальну вартість послуг.",
             "14": "Дано одну літеру. Визначити чи є вона голосною або приголосною.",
             "15": "Дано довжини трьох сторін трикутника. Визначити чи є трикутник рівностороннім або рівнобедреним."
             }

    # 1
    def task_1(self):
        name = input("Say us your name, please:\n")
        print("Hello, " + name + "!")

    # 2
    def task_2(self):
        a = int(input("Enter the 1st number, please:\n"))
        b = int(input("Enter the 2d number, please:\n"))
        c = int(input("Enter the 3d number, please:\n"))
        print(int.__add__(a, b).__add__(c))# три аргумента у __add__() выдали ошибку:D больше не работает(

    # 3
    def task_3(self):
        number = int(input("Enter number:\n"))
        prev = lambda x: x - 1
        next = lambda x: x + 1
        print("Next: " + str(number.__add__(1)))
        print("Prev: " + str(number.__sub__(1)))
        print("With lambdas: prev: " + str(prev(number)) + ", next: " + str(next(number)))

    # 4
    def task_4(self):
        s = int(input("Enter a square area:\n"))
        print("The square side is:\n" + str(math.sqrt(s)))

    # 5
    def task_5(self):
        a, b, c = [int(v) for v in input("Enter triangle sides lengths (space-separated):\n").split()]
        existence = lambda a, b, c: (a + b > c) and (b + c > a) and (c + a > b)
        while not existence(a, b, c):
            a, b, c = [int(v) for v in input("Enter lengths of sides of EXISTING triangle (space-separated):\n").split()]
        p = sum([a, b, c]) / 2
        print('Perimeter: ', p * 2)
        print('Square:', round(math.sqrt(p * (p - a) * (p - b) * (p - c)), 2))

    # 6
    def task_6(self):
        credit, interest = [float(v) for v in input("Enter a credit value and its interest (space-separated):\n").split()]
        interest = credit * interest / 100
        print("Refund is {} and interest value is {}.".format(credit + interest, interest))

    # 7
    def task_7(self):
        a, b = [int(v) for v in input(self.enter_2_nums).split()]
        ops = ["{} + {} = {}".format(a, b, a + b), "{} - {} = {}".format(a, b, a - b),
               "{} * {} = {}".format(a, b, a * b), "{} / {} = {}".format(a, b, a / b)]
        for op in ops:
            print(op)

    # 8
    def task_8(self):
        a, b = [int(v) for v in input(self.enter_2_nums).split()]
        random_int = random.randint(a, b)
        random_float = random.uniform(a, b)
        print(random_int, random_float, end='\n')

    # 9
    def task_9(self):
        a, b = [int(v) for v in input(self.enter_2_nums).split()]
        print(min([a, b]))

    # 10
    def sign(self, x, only_sign=False):
        if not only_sign:
            _sign = lambda a: (a > 0) - (a < 0)
            return _sign(x)
        else:
            if x == 0:
                return ""
            return "-" if x < 0 else "+"

    def task_10(self):
        number = int(input("Please, enter the number sign of what you wan to know:\n"))
        print(self.sign(number))

    # 11
    def task_11(self):
        a, b = [int(v) for v in input(self.enter_2_nums).split()]
        op = input("Enter operation:\n")
        while op not in ["*", "/", "+", "-"]:
            op = input("Enter permissible operation:\n")
        ops = {"+": int.__add__, "-": int.__sub__, "*": int.__mul__, "/": int.__truediv__}
        operation = lambda a, b, op: ops[op](a, b)
        print(a, op, b, "=", operation(a, b, op))

    # 12
    def task_12(self):
        global x1, x2
        a, b, c = [int(v) for v in input("Enter the coefficients of quadratic equation (space-separated):\n").split()]
        while a == 0:
            a = int(input("Please, enter not-null first coefficient for the equation being quadratic.\n"))
        d = (b ** 2) - (4 * a * c)
        if d >= 0:
            x1 = (-b - math.sqrt(d)) / (2 * a)
            x2 = (-b + math.sqrt(d)) / (2 * a)
        else:
            print("The discriminant is negative, so there is no rational solution for equation", end=" ")
        if abs(a) == 1:
            ft = "x^2" if self.sign(a, True) == "+" else "-x^2"
        else:
            ft = str(a) + "x^2"
        if b == 0:
            st = ""
        elif abs(b) == 1:
            st = str(self.sign(b, True)) + "x"
        else:
            st = str(self.sign(b, True)) + str(abs(b)) + "x"
        if c > 0:
            c = "+" + str(c)
        equation = ft + st + str(c) + "=0" if c != 0 else ft + st + "=0"
        print(equation)
        if d >= 0:
            print('The solution are {0} and {1}'.format(x1, x2))

    # 13
    def payment_amount(self, minutes, sms_amount):
        extra_mins = minutes - 100
        extra_sms = sms_amount - 30
        min_price = 0.30
        sms_price = 0.25
        extra_payment_for_sms = 0
        extra_payment_for_mins = 0
        if extra_sms > 0:
            extra_payment_for_sms = extra_sms * sms_price
        if extra_mins > 0:
            extra_payment_for_mins = extra_mins * min_price
        return 30 + extra_payment_for_mins + extra_payment_for_sms

    def task_13(self):
        minutes, sms = [int(v) for v in input("Enter the minutes and amount of sms you used (space-separated):\n").split()]
        print(self.payment_amount(minutes, sms))

    # 14
    def task_14(self):
        vowels = ["a", "e", "y", "i", "o", "u"]
        letter = input("Enter a letter:\n")
        print("Vowel" if letter in vowels else "Consonant")

    # 15
    def triangle_type(self, a, b, c):
        if a == b and b == c:
            return "Equilateral"
        elif a != b and b != c and a != c:
            return "Versatile"
        else:
            return "Isosceles"
    def task_15(self):
        a, b, c = [int(v) for v in input("Enter the sides of a triangle (space-separated):\n").split()]
        print(self.triangle_type(a, b, c))

class TaskChecking(object):

    def __init__(self):
        self.colours = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN]

    def check(self):
        lesson = Lesson1()
        columns = shutil.get_terminal_size().columns
        print(Style.BRIGHT + colored("1ST LESSON HOMEWORK:".center(columns), 'red', 'on_yellow'))
        tasks = lesson.tasks.keys()
        for i in range(len(tasks)):
            colour = random.choice(self.colours)
            print(Style.BRIGHT + colored(("Task " + str(i + 1)).center(columns), 'red', 'on_cyan'))
            print(colour + lesson.tasks.get(str(i + 1)))
            getattr(Lesson1, "task_" + str(i + 1))(lesson)

c = TaskChecking()
c.check()
