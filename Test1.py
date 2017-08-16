import random, math
from decimal import *
import numpy as np, pprint

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
#
# print("------------------------------------")
# print("Task 6 New")
# print("------------------------------------")
#
# def is_perfect(n):
#     s = Decimal(1)
#     p = Decimal(2)
#     while p < n.sqrt():
#         if n % p == 0:
#             s += p
#             if p != n/p:
#                 s += n/p
#         p += 1
#     return s == n
#
# print(is_perfect(Decimal('496')))
#
# def is_perfect_number(n):
#     s = 0
#     for j in range(1, n):
#         if n % j == 0:
#             s += j
#     if s == n:
#         return True
#     else:
#         return False
#
# print(is_perfect_number(496))
# print(is_perfect_number(7497))

# print("------------------------------------")
# print("Task 10")
# print("------------------------------------")
#
# import numpy as np, pprint
# matrix = np.array([[0, 1, 2],
#               [4, 5, 6],
#               [7, 8, 9],
#               [10, 11, 12],
#               [13, 14, 15],
#               [16, 17, 18],
#               [19, 20, 21],
#               [22, 23, 24]])
#
# transpose_matrix = matrix.transpose()
#
# pprint.pprint(matrix)
# pprint.pprint(transpose_matrix)
#
print("------------------------------------")
print("Task 11")
print("------------------------------------")

matrix = []
numb_of_columns_horiz = 3
numb_of_colums_ver = 5

def create_matrix (matrix, numb_of_columns_horiz, numb_of_colums_ver):
    for i in range(numb_of_colums_ver):
        columns_horiz = []
        for x in range(numb_of_columns_horiz):
            numb = random.randrange(5)
            columns_horiz.append(numb)
        matrix.append(columns_horiz)
    return matrix

def transpose_matrix(matrix):
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in matrix[i]:
            print(j, end="\t")
        print()

def sort (matrix):
    for i in range (len(matrix)):
        if i % 2:
            matrix[i].sort()
        else:
            matrix[i].sort(reverse=True)
    return matrix


original_matrix = create_matrix(matrix, numb_of_columns_horiz, numb_of_colums_ver)
original_matrix1 = np.array(original_matrix)
transpose_matrix1 = original_matrix1.transpose()
print(transpose_matrix1)

print("Original matrix:\n", original_matrix)
print("Sorted matrix:")
print_matrix(transpose_matrix(sort(original_matrix)))

print("------------------------------------")
print("Task 12")
print("------------------------------------")

lst1 = [i for i in range(2,10)]
lst2 = [i for i in range(2,10)]

def tasks_for_children (lst1, lst2):
    numbers_of_tasks = 0
    lst_of_tasks = []
    while numbers_of_tasks < 15:
        x = random.choice(lst1)
        y = random.choice(lst2)
        task1 = ("%a * %a" % (x, y))
        task2 = ("%s * %s" % (y, x))
        if task1 in lst_of_tasks:
            continue
        elif task2 in lst_of_tasks:
            continue
        else:
            lst_of_tasks.append(task1)
        numbers_of_tasks += 1
    return lst_of_tasks

print(tasks_for_children(lst1,lst2))

