import math
from datetime import datetime,date

print("------------------------------------")
print("Task 1-6")
print("------------------------------------")

a = 10
b = 11
c = 180

p = (a + b * (c / 2))
print(p)

p = (a ** 2 + b ** 2) % 2
print(p)

p = (a + b) / 12 * c % 4 + b
print(p)

p = (a - b * c) / (a + b) % c
print(p)

p = abs(a - b) / (a + b) ** 3 - math.cos(c)
print(p)

p = ((math.log(1+c)/-b**4)+abs(a))
print(p)


print()
print("------------------------------------")
print("Task 7")
print("------------------------------------")

american_date = "23.11.1092"
print("American format date", american_date)
lst1 = american_date.split(".")
european_date = lst1[1] + "." + lst1[0] + "." + lst1[2]
print("European format date:", european_date)

print()
print("Other way to solve this task")
print()

date = date(2016,1,17)
american_date = date.strftime('%m,%d,%Y')
european_date = date.strftime('%d,%m,%Y')
print("American format date:", american_date)
print("European format date:", european_date)


print()
print("------------------------------------")
print("Task 8")
print("------------------------------------")

str1 = "Hello World!"
str2 = "Hi there!"
middle1 = len(str1)//2
middle2 = len(str2)//2
str3 = str2[:middle2] + str1 + str2[middle2:]
str4 = str1[:middle1] + str3 + str1[middle1:]
print("Результат \"ахинея получилась\":", str4)


print()
print("------------------------------------")
print("Task 9")
print("------------------------------------")

words = "bill pitch goal"
words_lst = words.split(" ")
words_lst[1] = words_lst[1].upper()
words_lst = " ".join(words_lst)
print("The result: second word should be in uppercase -", words_lst)

print()
print("------------------------------------")
print("Task 10")
print("------------------------------------")

task = "Leo Tolstoy*1828-08-28*1910-11-20"
lst = task.split('*')
name = lst[0]
date1 = lst[1]
date2 = lst[2]
year1 = int(date1.split('-')[0])
year2 = int(date2.split('-')[0])
age = year2 - year1
print("Name of the writer: %s, age %d" % (name, age))

print()
print("------------------------------------")
print("Task 11")
print("------------------------------------")

def degree_to_radian (value):
    rad = value * math.pi/180
    print("Cosine of %s degree is: %.4f" % (value, math.cos(rad)))
    return rad

degree_to_radian(40)
degree_to_radian(45)
degree_to_radian(60)


print("------------------------------------")
print("Task 12")
print("------------------------------------")

# n = int(input("Введите трехзначное число: "))
# def sum_numbers(n):
#     a = n % 10
#     b = n % 100//10
#     c = n // 100
#     return a+b+c
# sum = sum_numbers(n)
# print("Сумма цифр числа:", sum)


print("------------------------------------")
print("Task 13")
print("------------------------------------")

def square_perimeter_rectangle (a,b):
    rectangal_square = 1/2*a*b
    hypotenuse = math.sqrt(a ** 2 + b ** 2)
    rectangal_perimeter = hypotenuse+a+b
    return rectangal_square, rectangal_perimeter

s, p = square_perimeter_rectangle(4,10)
print("Площадь прямого треугольника равна: %.2a\nПериметр прямого треугольника равен: %s" % (s, round(p,2)))

print("------------------------------------")
print("Task 14")
print("------------------------------------")

number = int(input("Введите число: "))
def even(n):
    if n%2:
        return False
    else:
        return True
d = even(number)
if even(d):
    print("%d isn't even" % number)
else:
    print("%d is even" % number)


print("------------------------------------")
print("Task 15")
print("------------------------------------")

