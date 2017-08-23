import math, random, string, pickle, json, requests
from datetime import datetime,date
from random import shuffle
from pprint import pprint

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
# print("------------------------------------")
# print("Task 19")
# print("------------------------------------")
#
#
# range_num = int(input("Enter number of random numbers: "))
# random_num = int(input("Enter the maximum value for the range: "))
#
#
# def search_of_arithmetic_mean (range_num, random_num):
#     total_sum = 0
#     for i in range(range_num):
#         number = random.randint(0, random_num)
#         print(number)
#         total_sum += number
#     arithmetic_mean = total_sum/range_num
#     return arithmetic_mean
#
# # result = (search_of_arithmetic_mean(range_num, random_num))
# print("The arithmetic mean for %d randomly generated numbers between 0 and %d is: %.2f" % (range_num, random_num, search_of_arithmetic_mean(range_num, random_num)))


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
#
# print("------------------------------------")
# print("Task 24")
# print("------------------------------------")
#
# print("Я загадал число от 1 до 10! Попробуйте угадать!")
#
# random_num= random.randint(1, 10)
# while True:
#     choice = int(input("Введите ваше число:"))
#     if 1 <= choice <= 10:
#         if choice == random_num:
#             print("Вы угадали! Поздравляю.")
#             break
#         elif choice > random_num:
#             print("Направильный ответ, загаданное число меньше")
#         elif choice < random_num:
#             print("Направильный ответ, загаданное число больше")
#
#     else:
#         print("Не правильное значение, необходимо указать цифру от 1 до 10")
#
#
# print("------------------------------------")
# print("Task 25")
# print("------------------------------------")
#
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
#
# print(factorial(3))
#
# print("------------------------------------")
# print("Task 26")
# print("------------------------------------")
#
# def simple_numbers (number):
#     if not number % 2 and number // 2 != 1:
#         return False
#     elif not number % 3 and number // 3 != 1:
#         return False
#     elif not number % 5 and number // 5 != 1:
#         return False
#     elif not number % 7 and number // 7 != 1:
#         return False
#     else:
#         return True
#
# start_digit = 1
# end_digit = 100
# print ("Все простые числа от %d до %d :" %(start_digit, end_digit))
#
# for i in range(start_digit, end_digit):
#     if simple_numbers(i):
#         print (i)

# print("------------------------------------")
# print("Task 27")
# print("------------------------------------")
#
# def odd_numbers (n):
#     list =[]
#     for i in range (0,n):
#         if i%2 !=0:
#             list.append(i)
#     return list
# odds_list = odd_numbers(100)
# odd_str = " ".join([str(c) for c in odds_list])
# print(odd_str)
#
# random_odds_list = [odds_list for odds_list in range(100) if odds_list % 2 != 0]
# shuffle(random_odds_list)
# random_odds_str = " ".join([str(a) for a in random_odds_list])
# print(random_odds_str)
#
# print("------------------------------------")
# print("Task 28")
# print("------------------------------------")
#
# lst1=([random.randint(0,5) for i in range(5)])
# lst2=([random.randint(0,5) for i in range(5)])
# print("Первый список: %s" % (" ".join([str(c) for c in lst1])))
# print("Второй список: %s" % (" ".join([str(c) for c in lst2])))
#
# avg_lst1 = sum(lst1)/len(lst1)
# avg_lst2 = sum(lst2)/len(lst2)
# print(avg_lst1)
# print(avg_lst2)
#
# if avg_lst1 > avg_lst2:
#     print("Среднее арифметическое списка один больше среднего арифметического списка два")
# elif avg_lst1 < avg_lst2:
#     print("Среднее арифметическое списка один меньше среднего арифметического списка два")
# elif avg_lst1 == avg_lst2:
#     print("Среднее арифметическое списка один равно среднему арифметическому списка два")
#
# print("------------------------------------")
# print("Task 29")
# print("------------------------------------")
#
# lst = ([random.randint(-1, 1) for i in range(11)])
# print("Строка случайных целых чисел: %s" % (", ".join([str(i) for i in lst])))
#
# if (lst.count(-1) > lst.count(0)) and (lst.count(-1) > lst.count(1)):
#     print("Чащего всего в списке встречается число: -1")
# elif (lst.count(0) > lst.count(-1)) and (lst.count(0) > lst.count(1)):
#     print("Чащего всего в списке встречается число: 0")
# elif (lst.count(1) > lst.count(-1)) and (lst.count(1) > lst.count(0)):
#     print("Чащего всего в списке встречается число: 1")
# else:
#     print()
#
# print("------------------------------------")
# print("Task 30")
# print("------------------------------------")
#
# def encrypt_text(input_str):
#     crypto_table = [chr(i) for i in range(ord('A'), ord('z') + 1)] + [chr(i) for i in range(ord("А"), ord("я")+1)] + [chr(i) for i in range(ord(' '), ord('?') + 1)]
#     encrypted_text = []
#     for i in input_str:
#         char_id = (crypto_table.index(i) + 5) % len(crypto_table)
#         encrypted_text.append(crypto_table[char_id])
#     return encrypted_text
#
# user_input = input("Введите произвольную строку символов: ")
# print("Зашифрованная введнная строка: ", "".join(encrypt_text(user_input)))

# print("------------------------------------")
# print("Task 31")
# print("------------------------------------")
#
# def create_password(pswd_len = 9):
#     all_symbols = list(random.choice(string.ascii_lowercase)) + list(random.choice(string.ascii_uppercase)) + list(random.choice(string.digits))
#     i = 0
#     pswd = ["_"] + all_symbols
#     len_index = len(pswd)
#     while i < (pswd_len - len_index):
#         pswd.append(random.choice(all_symbols))
#         i += 1
#     random.shuffle(pswd)
#
#     return "".join(pswd)
#
# print("Generated password:", create_password())
#
# print("------------------------------------")
# print("Task 32")
# print("------------------------------------")
#
# phone_book = [
#               {"name": "Petr", "surname": "Petrov", "age": 50, "phone_number":"+380501234567", "skype_login": "qwe"},
#               {"name": "Ivan", "surname": "Ivanov", "age": 15, "phone_number":"+380507654321", "skype_login": "asd"},
#              ]
#
# def print_entry(number, entry):
#     print ("--[ %s ]--------------------------" % number)
#     print ("| Surname:     %20s |" % entry["surname"])
#     print ("| Name:        %20s |" % entry["name"])
#     print ("| Age:         %20s |" % entry["age"])
#     print("| Phone number: %20s |" % entry["phone_number"])
#     print("| Skype:        %20s |" % entry["skype_login"])
#     print ()
#
#
# def print_phonebook():
#     print ()
#     print ()
#     print ("#########  Phone book  ##########")
#     print ()
#
#     number = 1
#     for entry in phone_book:
#         print_entry(number, entry)
#         number += 1
#
# def print_phonebook_by_age():
#     phone_book.sort(key=lambda contact: contact['age'])
#     print_phonebook()
#
# def add_entry_phonebook(surname, name, age, phone_number, skype_login):
#     entry = {}
#     entry["surname"] = surname
#     entry["name"] = name
#     entry["age"] = age
#     entry["phone_number"] = phone_number
#     entry["skype_login"] = skype_login
#     phone_book.append(entry)
#
# def printError(message):
#     print ("ERROR: %s" % message)
#
# def printInfo(message):
#     print ("INFO: %s" % message)
#
# def find_entry_name_phonebook(name):
#     idx = 1
#     found = False
#     for entry in phone_book:
#         if entry["name"] == name:
#             print_entry(idx, entry)
#             idx += 1
#             found = True
#     if not found:
#         printError("Not found!!")
#
#
# def find_entry_age_phonebook(age):
#     idx = 1
#     found = False
#     for entry in phone_book:
#         if entry["age"] == age:
#             print_entry(idx, entry)
#             idx += 1
#             found = True
#     if not found:
#         printError("Not found!!")
#
# def find_entry_phone_number(phone_number):
#     idx = 1
#     found = False
#     for contact in phone_book:
#         if contact["phone_number"] == phone_number:
#             print_entry(idx, contact)
#             idx += 1
#             found = True
#     if not found:
#         printError("Not found!!")
#
# def find_entry_skype_login(skype_login):
#     idx = 1
#     found = False
#     for contact in phone_book:
#         if contact["skype_login"] == skype_login:
#             print_entry(idx, contact)
#             idx += 1
#             found = True
#     if not found:
#         printError("Not found!!")
#
# def delete_entry_name_phonebook(name):
#     idx = 1
#     found = False
#     for contact in phone_book:
#         if contact['name'] == name:
#             print_entry(idx, contact)
#             phone_book.remove(contact)
#             idx += 1
#             found = True
#             print("This contact was removed from Phone book.")
#     if not found:
#         printError("Not found!!")
#
# def count_all_entries_in_phonebook():
#     print ("Total number of entries: ", len(phone_book))
#
# def print_avr_age():
#     total_age = 0
#     for contact in phone_book:
#         year = contact["age"]
#         total_age += year
#     avg_age = total_age // len(phone_book)
#     print('Average age is :', (avg_age))
#
# def increase_age(number_of_years):
#     for contact in phone_book:
#         contact["age"] += number_of_years
#
# def add_entry_skype_name(name):
#     idx = 1
#     found = False
#     for contact in phone_book:
#         if contact["name"] == name:
#             skype = str(input("Please enter Skype login for current user: "))
#             contact["skype_login"] = skype
#             print_entry(idx, contact)
#             found = True
#     if not found:
#         printError("Not found!!")
#
# def save_to_file():
#     pickle.dump(phone_book, open("phone_book.save", "wb"))
#     printInfo("Phonebook is saved into 'phone_book.save'")
#
#
# def load_from_file():
#     global phone_book
#     phone_book = pickle.load(open("phone_book.save", "rb"))
#     printInfo("Phonebook is loaded from 'phone_book.save'")
#
#
# def main():
#     while True:
#         user_input = ""
#         try:
#             print ()
#             print ()
#             print ()
#             print("~ Welcome to phonebook ~")
#             print("Select one of actions below:")
#             print("    1 - Print phonebook entries")
#             print("    2 - Print phonebook entries (by age)")
#             print("    3 - Add new entry")
#             print("    4 - Find entry by name")
#             print("    5 - Find entry by age")
#             print("    6 - Find entry by phone number")
#             print("    7 - Find entry by skype name")
#             print("    8 - Delete entry by name")
#             print("    9 - The number of entries in the phonebook")
#             print("    10 - Avr. age of all persons")
#             print("    11 - Increase age by num. of years")
#             print("    12 - Add Skype for existing contacts")
#             print("-----------------------------")
#             print("     s - Save to file")
#             print("     l - Load from file")
#             print("     0 - Exit")
#
#             user_input = input("Enter you choice: ")
#             choice = int(user_input)
#
#             if choice == 1:
#                 print_phonebook()
#             elif choice == 2:
#                 print_phonebook_by_age()
#             elif choice == 3:
#                 surname = str(input("    Enter surname: "))
#                 name = str(input("    Enter name: "))
#                 age = int(input("    Enter age: "))
#                 phone_number = str(input("    Enter a phone number (Ex. +380501234567):"))
#                 skype_name = str(input("    Enter a skype name:"))
#                 add_entry_phonebook(surname, name, age, phone_number, skype_name)
#             elif choice == 4:
#                 name = str(input("    Enter name: "))
#                 find_entry_name_phonebook(name)
#             elif choice == 5:
#                 age = int(input("    Enter age: "))
#                 find_entry_age_phonebook(age)
#             elif choice == 6:
#                 phone_number = str(input("    Enter phone number: "))
#                 find_entry_phone_number(phone_number)
#             elif choice == 7:
#                 skype_name = str(input("    Enter Skype login: "))
#                 find_entry_skype_login(skype_name)
#             elif choice == 8:
#                 name = str(input("    Enter name: "))
#                 delete_entry_name_phonebook(name)
#             elif choice == 9:
#                 count_all_entries_in_phonebook()
#             elif choice == 10:
#                 print_avr_age()
#             elif choice == 11:
#                 nmbrs_of_years = int(input("    Enter number of years to add to current ages: "))
#                 increase_age(nmbrs_of_years)
#             elif choice == 12:
#                 name = str(input("    Enter name: "))
#                 add_entry_skype_name(name)
#             elif choice == 0:
#                 print ("Bye!")
#                 break
#             else:
#                 print ("Enter action within range [0..9]")
#
#         except ValueError:
#             if str(user_input) == 's':
#                 save_to_file()
#             elif str(user_input) == 'l':
#                 load_from_file()
#             else:
#                 printError("Something went wrong. Try again...")
#
#
# if __name__ == '__main__':
#     main()
#
print("------------------------------------")
print("Task 33")
print("------------------------------------")

#------------------------------------------------------------------------------
BASE_URL = "http://54.201.47.219:8080/api"
VERSION  = "v1"
URL = "%s/%s" % (BASE_URL, VERSION)

#------------------------------------------------------------------------------
def log_error(msg):
    print("ERROR: ", msg)

#------------------------------------------------------------------------------
def get_students():
    response = requests.get(URL + '/students')
    result = None
    if response.status_code == 200:
        json_object = response.json()
        result = json_object['students']
    else:
        log_error(response.content)

    return result

# ------------------------------------------------------------------------------
def get_student(id):
    response = requests.get(URL + '/students/' + str(id))
    result = None
    if response.status_code == 200:
        json_object = response.json()
        result = json_object['student']
    else:
        log_error(response.content)

    return result

#------------------------------------------------------------------------------
def update_student(id, upd_fields):
    response = requests.put(URL + '/students/' + str(id), json=json.dumps(upd_fields))
    result = response.status_code == 200
    if not result:
        log_error(response.content)

    return result

#------------------------------------------------------------------------------
def add_student(student):
    response = requests.post(URL + '/students/', json=json.dumps(student))
    result = response.status_code == 200
    if not result:
        log_error(response.content)

    return result

#------------------------------------------------------------------------------
def reset():
    response = requests.put(URL + '/reset')
    result = response.status_code == 200
    if not result:
        log_error(response.content)

    return result

# ------------------------------------------------------------------------------
def demo():
    '''
    Demonstrates fetching, updating and adding new student.
    Resets remote DB afterwards
    :return: None
    '''

    # available urls
    # http://54.201.47.219:8080/api/v1/students/
    # http://54.201.47.219:8080/api/v1/students/1025
    # http://54.201.47.219:8080/api/v1/hw_results/
    # http://54.201.47.219:8080/api/v1/hw_results/1025
    # http://54.201.47.219:8080/api/v1/test1_results/
    # http://54.201.47.219:8080/api/v1/test1_results/1025
    # http://54.201.47.219:8080/api/v1/test1_weights/

    # pprint(get_students())
    #
    # pprint(get_student(1024))
    # update_student(1024, {'rank': 42})
    # pprint(get_student(1024))
    #
    # add_student({"id": 1234, "fullname": "AAAA", "email": "x@y.z", "github": "", "rank": 0})
    # pprint(get_student(1234))
    #
    # reset()
    # pprint(get_students())
    update_students_results()
    pprint(print_students_info())

# ------------------------------------------------------------------------------
def get_test1_results():
    response = requests.get(URL + '/test1_results/')
    result = None
    if response.status_code == 200:
        json_object = response.json()
        result = {i['id']: i['task_completion'] for i in json_object}
    else:
        log_error(response.content)

    return result

# ------------------------------------------------------------------------------
def get_test1_weights():
    response = requests.get(URL + '/test1_weights')
    result = None
    if response.status_code == 200:
        json_object = response.json()
        result = json_object['test1_weights']
    else:
        log_error(response.content)

    return result

# ------------------------------------------------------------------------------
def get_hw_results():
    response = requests.get(URL + '/hw_results')
    result = None
    if response.status_code == 200:
        json_object = response.json()
        result = {i['id']: i['task_completion'] for i in json_object}
    else:
        log_error(response.content)

    return result

# ------------------------------------------------------------------------------
def get_student_hw_results(id):
    response = requests.get(URL + '/hw_results/' + str(id))
    result = None

    if response.status_code == 200:
        json_object = response.json()
        result = json_object['task_completion']
    else:
        log_error(response.content)

    return result

# ------------------------------------------------------------------------------
def update_students_results():
    '''
    Calculate student results and put them into the student dictionary under the key "rank".
    Total rank is calculated as a sum of completed hw tasks +
        sum of completed Test1 tasks weighted proportional to its weights.
    For example, student with id=1025 has total rank = 1*32 + (1*1 + 1*1 + 1*1 + ... 1*15) = 68)
    :return: None
    '''
    students = get_students()
    hw_result = get_hw_results()
    test1_results = get_test1_results()
    test1_weights = get_test1_weights()
    for student in students:
        stud_id = student['id']
        hw_rank = hw_result[stud_id]
        test1_rank = test1_results[stud_id]
        total_rank = sum(hw_rank)
        for i in range(len(test1_rank)):
            total_rank += int(test1_rank[i]) * int(test1_weights[i])
        update_student(stud_id, {'rank': total_rank})

# ------------------------------------------------------------------------------
def print_students_info(sort_by_key="fullname"):
    '''
    Prints students info sorted according to the passed key in dictionary). By default, sort by students names.
    Student info should be presented as a card that includes the following information:
        - id,
        - name,
        - email,
        - github account (only name, not URL path)
        - rank
    Example (format is not strictly required):
        -----------------------------------------
        : ID:                               1025:
        :.......................................:
        : Full name:                Юношев Павел:
        : Email:          p.n.yunoshev@gmail.com:
        : Github:                               :
        : Rank:                               42:
        -----------------------------------------
    :return: None
    '''
    students = get_students()
    students.sort(key=lambda student: student[sort_by_key])
    for people in students:
        print("_" * 50)
        print(": ID:         %34s :" % people['id'])
        print("-" * 50)
        print(": Full name:  %34s :" % people['fullname'])
        print(": Email:      %34s :" % people['email'])
        git = people['github'].split('/')
        if len(git) >=4:
            print(": Github: %38s :" % git[3])
        else:
            print((': Github:' + ' '*6 + "Student don't have Github account :"))
        print(": Rank:       %34s :" % people['rank'])
        print("_"*50)
    
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    demo()