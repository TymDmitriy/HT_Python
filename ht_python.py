import math, random
from datetime import datetime,date
#
# print("------------------------------------")
# print("Task 1-6")
# print("------------------------------------")
#
# a = 10
# b = 11
# c = 180
#
# p = (a + b * (c / 2))
# print(p)
#
# p = (a ** 2 + b ** 2) % 2
# print(p)
#
# p = (a + b) / 12 * c % 4 + b
# print(p)
#
# p = (a - b * c) / (a + b) % c
# print(p)
#
# p = abs(a - b) / (a + b) ** 3 - math.cos(c)
# print(p)
#
# p = ((math.log(1+c)/-b**4)+abs(a))
# print(p)
#
#
# print()
# print("------------------------------------")
# print("Task 7")
# print("------------------------------------")
#
# american_date = "23.11.1092"
# print("American format date", american_date)
# lst1 = american_date.split(".")
# european_date = lst1[1] + "." + lst1[0] + "." + lst1[2]
# print("European format date:", european_date)
#
# print()
# print("Other way to solve this task")
# print()
#
# date = date(2016,1,17)
# american_date = date.strftime('%m,%d,%Y')
# european_date = date.strftime('%d,%m,%Y')
# print("American format date:", american_date)
# print("European format date:", european_date)
#
#
# print()
# print("------------------------------------")
# print("Task 8")
# print("------------------------------------")
#
# str1 = "Hello World!"
# str2 = "Hi there!"
# middle1 = len(str1)//2
# middle2 = len(str2)//2
# str3 = str2[:middle2] + str1 + str2[middle2:]
# str4 = str1[:middle1] + str3 + str1[middle1:]
# print("Результат \"ахинея получилась\":", str4)
#
#
# print()
# print("------------------------------------")
# print("Task 9")
# print("------------------------------------")
#
# words = "bill pitch goal"
# words_lst = words.split(" ")
# words_lst[1] = words_lst[1].upper()
# words_lst = " ".join(words_lst)
# print("The result: second word should be in uppercase -", words_lst)
#
# print()
# print("------------------------------------")
# print("Task 10")
# print("------------------------------------")
#
# task = "Leo Tolstoy*1828-08-28*1910-11-20"
# lst = task.split('*')
# name = lst[0]
# date1 = lst[1]
# date2 = lst[2]
# year1 = int(date1.split('-')[0])
# year2 = int(date2.split('-')[0])
# age = year2 - year1
# print("Name of the writer: %s, age %d" % (name, age))
#
# print()
# print("------------------------------------")
# print("Task 11")
# print("------------------------------------")
#
# def degree_to_radian (value):
#     rad = value * math.pi/180
#     print("Cosine of %s degree is: %.4f" % (value, math.cos(rad)))
#     return rad
#
# degree_to_radian(40)
# degree_to_radian(45)
# degree_to_radian(60)
#
#
# print("------------------------------------")
# print("Task 12")
# print("------------------------------------")
#
# n = int(input("Введите трехзначное число: "))
# def sum_numbers(n):
#     a = n % 10
#     b = n % 100//10
#     c = n // 100
#     return a+b+c
# sum = sum_numbers(n)
# print("Сумма цифр числа:", sum)
#
#
# print("------------------------------------")
# print("Task 13")
# print("------------------------------------")
#
# def square_perimeter_rectangle (a,b):
#     rectangal_square = 1/2*a*b
#     hypotenuse = math.sqrt(a ** 2 + b ** 2)
#     rectangal_perimeter = hypotenuse+a+b
#     return rectangal_square, rectangal_perimeter
#
# s, p = square_perimeter_rectangle(4,10)
# print("Площадь прямогоугольного треугольника равна: %.2a"
#       "\nПериметр прямогоугольного треугольника равен: %s" % (s, round(p,2)))
#
# print("------------------------------------")
# print("Task 14")
# print("------------------------------------")
#
# number = int(input("Введите число: "))
# def even(n):
#     if n%2==0:
#         return False
#     else:
#         return True
# d = even(number)
# if even(d):
#     print("%d isn't even" % number)
# else:
#     print("%d is even" % number)
#
#
# print("------------------------------------")
# print("Task 15")
# print("------------------------------------")
#
#
# def circles (x1, y1, r1, x2, y2, r2):
#     circle_lenght = math.sqrt((x2-x1)**2+(y2-y1)**2)
#     if (r2+r1) >= circle_lenght and abs((r1-r2)) <= circle_lenght:
#         return True
#     else:
#         return False
#
# x1 = 1
# y1 = 4
# r1 = 1
#
# x2 = 1
# y2 = 2
# r2 = 1
#
#
# if circles (x1, y1, r1, x2, y2, r2):
#     print("Circles cross ")
# else:
#     print("Circles don't cross")
#
#
# print("------------------------------------")
# print("Task 16")
# print("------------------------------------")
#
# v1 = int(input("Ведите скорость первого поезда:"))
# v2 = int(input("Ведите скорость второго поезда:"))
#
# def trains_not_crush (v1, v2, s=10, s1=4):
#     if s1/v1 <= (s-s1)/v2:
#         return True
#     else:
#         return False
#
# if trains_not_crush (v1,v2):
#     print("\nIt was close")
# else:
#     print("\nCrush")
#
#
# print("------------------------------------")
# print("Task 17")
# print("------------------------------------")
#
# def quadratic_equation (a, b, c):
#     D = b**2 - 4*a*c
#     if D > 0:
#         x1 = (-b + math.sqrt(D)) / (2 * a)
#         x2 = (-b - math.sqrt(D)) / (2 * a)
#         return round(x1, 3), round(x2, 3)
#     if D == 0:
#         x1 = x2 = -b / (2*a)
#         return round(x1, 3), round(x2, 3)
#     else:
#         return "Has no solution"
#
# a = float(input("Enter a value for a:"))
# b = float(input("Enter a value for b:"))
# c = float(input("Enter a value for c:"))
#
# result = quadratic_equation(a,b,c)
# print("\nFor current quadratic_equation:", result)
#
# print("------------------------------------")
# print("Task 18")
# print("------------------------------------")
#
# symbol1 = ord(input("Please write first symbol: "))
# symbol2 = ord(input("Please write second symbol: "))
#
# def total_sum_symbols (a, b):
#     symb_sum = 0
#     for i in range (a,b+1):
#         symb_sum += i
#     print("Total sum of Unicode is: ", symb_sum)
#
#
# if symbol1 <= symbol2:
#     total_sum_symbols(symbol1, symbol2)
# else:
#     total_sum_symbols(symbol2, symbol1)
#
print("------------------------------------")
print("Task 19")
print("------------------------------------")


range_num = int(input("Enter number of random numbers: "))
random_num = int(input("Enter the maximum value for the range: "))


def search_of_arithmetic_mean (range_num, random_num):
    total_sum = 0
    for i in range(range_num):
        number = random.randint(0, random_num)
        print(number)
        total_sum += number
    arithmetic_mean = total_sum/range_num
    return arithmetic_mean

# result = (search_of_arithmetic_mean(range_num, random_num))
print("The arithmetic mean for %d randomly generated numbers between 0 and %d is: %.2f" % (range_num, random_num, search_of_arithmetic_mean(range_num, random_num)))


# print("------------------------------------")
# print("Task 20")
# print("------------------------------------")
#
# lst_begin = int(input("Enter lower bound of your list: "))
# lst_end = int(input("Enter upper bound of your list: "))
#
# def difference_between_odds_evens (lst_begin, lst_end):
#     lst = list(range(lst_begin,lst_end+1))
#     print(lst)
#     odds_sum = 0
#     even_sum = 0
#     for i in range (lst_begin, lst_end+1):
#         if i%2==0:
#             even_sum += i
#         else:
#             odds_sum += i
#     return even_sum-odds_sum
#
# print(difference_between_odds_evens (lst_begin, lst_end))
#
# print("------------------------------------")
# print("Task 21")
# print("------------------------------------")
#
# def is_included (numbers, basis):
#     while numbers >=1:
#         digit = numbers%10
#         if digit == basis:
#             return True
#         numbers //= 10
#     return False
#
# numbers = 1000
# digits1 = 1
# digits2 = 7
#
# for i in range(1,numbers+1):
#     if is_included(i,digits1) and is_included(i,digits2):
#         print (i)
#
# print("------------------------------------")
# print("Task 22")
# print("------------------------------------")
#
# def sum_exponentiation (number=3,boundary_value=1000000):
#     sum_number = 0
#     i = 0
#     while sum_number < boundary_value:
#         sum1 = number**i
#         i += 1
#         if sum1 <= boundary_value:
#             sum_number += sum1
#         else:
#             break
#     return sum_number
#
# print("Total sum of numbers, which are a power of 3 is:", sum_exponentiation())
#
# print("------------------------------------")
# print("Task 23")
# print("------------------------------------")
#
# def max_digit_in_number ():
#     lst = random.randint(10**11, 10**12-1)
#     print(lst)
#     max_number = max([int(i) for i in str(lst)])
#     return max_number, lst
#
# print("Max digit is %d in value %d" % max_digit_in_number())

# print("------------------------------------")
# print("Task 24")
# print("------------------------------------")

