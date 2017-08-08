import random, math
from decimal import *

# print("------------------------------------")
# print("Task 1-3")
# print("------------------------------------")
#
# a = int(input("Введите значение а:"))
# b = int(input("Введите значение b:"))
# c = int(input("Введите значение c:"))
#
# print("(a+b*c)**2 = %d, a-4*b/c = %.2f, (a*b+4)/(c-1) = %d" % ((a+b*c)**2, a-4*b/c, (a*b+4)/(c-1)))
#
# print("------------------------------------")
# print("Task 4")
# print("------------------------------------")
#
# product=1
# while True:
#     n = input("Введите 5-значное число:")
#     if len(n)==5:
#         for i in n:
#             if int(i) % 2 != 0:
#                 product = product * int(i)
#         break
#     else:
#         print("Невернны ввод.Введите 5-значное число")
# print(product)
#
# print("------------------------------------")
# print("Task 5")
# print("------------------------------------")
#
# num1=float(input("Введите первое значение:"))
# num2=float(input("Введите второе значение:"))
# goal=10
#
# if abs(num1-goal)>abs(num2-goal):
#     print(num2, "Ближе к", goal)
# elif abs(num2-goal)>abs(num1-goal):
#     print(num1, "Ближе к", goal)
# else:
#     print("Введенные значения находятся на равном расстоянии от", goal)
#
# print("------------------------------------")
# print("Task 6")
# print("------------------------------------")
#
#
# primes = lambda rang: [num for num in range(2, rang) if not 0 in map(lambda z: num % z, range(2, int((math.sqrt(num)+1))))]
# print([random.choice(list(map(int, primes(10**2)))) for i in range(10)])
#
# print("------------------------------------")
# print("Task 7")
# print("------------------------------------")
#
# def fibonacci_number(n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci_number(n-1) + fibonacci_number(n-2)
#
#
# sum=0
# numbers=10
# for i in range(numbers):
#     sum+=fibonacci_number(i)
# print(sum)
#
# print("------------------------------------")
# print("Task 8")
# print("------------------------------------")
#
# lst = [random.randint(200,1000) for i in range(20)]
# print(lst)
# min=lst.index(min(lst))
# max=lst.index(max(lst))
# lst[min], lst[max] = lst[max], lst[min]
# print(lst)
#
# print("------------------------------------")
# print("Task 9")
# print("------------------------------------")
#
# random_lst=[random.randint(-42,42)for i in range(20)]
# print("Массив случайных чисел:",random_lst)
# lst=[round(i/max([abs(i) for i in random_lst]), 3) for i in random_lst]
# lst.sort()
# print("Нормированный массив:",lst)

print("------------------------------------")
print("Task 6 New")
print("------------------------------------")

def is_perfect(n):
    s = Decimal(1)
    p = Decimal(2)
    while p < n.sqrt():
        if n % p == 0:
            s += p
            if p != n/p:
                s += n/p
        p += 1
    return s == n

print(is_perfect(Decimal('496')))

def is_perfect_number(n):
    s = 0
    for j in range(1, n):
        if n % j == 0:
            s += j
    if s == n:
        return True
    else:
        return False

print(is_perfect_number(496))
print(is_perfect_number(7497))

