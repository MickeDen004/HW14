"""Генератор - это объект, который сразу
при создании не вычисляет значения всех своих элементов

Он хранит в памяти только последний вычеленный элемент,
правило перехода к следующему и условие, при котором выполнение
прерывается.

Вычисление следующего значения происходит лишь
при выполнении метода next(). Предыдущее значение при этом теряется.

В этом и заключаетс] отличие списков от генераторов: в списках
все элементы хоанятся в памяти, их можно удалить только программно.

Вычисления с помощью генераторов называются ленивыми, они экономят память.

Рассмотрим пример: создадим обьект-генератор gen с помощью так называемого генераторного выражения.
Счет квдратов чисел от 1 до 4

"""

a = (i**2 for i in range(1,5))
for i in a:
    print(i, type(a))


def f_gen(m):
    s = 1
    for n in range(1, m):
        yield n**2 + s
        s += 1

print(a)
a = f_gen(5)
for i in a:
    print(i)

# Infinite sequence

# import math
#
#
# def prime_num():
#     nm = 2
#     while True:
#         sq = math.ceil(nm**1/2)
#         for i in range(2, sq+1):
#             if (nm % i) == 0:
#                 break
#             else:
#                 yield nm
#                 nm += 1
#
#
# for num in prime_num():
#     print(num)


# next, close, throw, send

# def f_gen():
#     n = 1
#     while True:
#         yield n**2
#         n += 1
#
# generator1 = f_gen()
# generator2 = f_gen()
#
# for i in generator1:
#     print(i)
#     if i > 10:
#         generator1.close()
#
#
# for i in generator2:
#     print(i)
#     if i > 20:
#         generator2.throw(Exception('Bad!'))

print("Natural numbers from 1 to 5")
def natural_numbers():
    num = 1
    while num <= 5:
        yield num
        num += 1
for i in natural_numbers():
    print(f"{i**-1/2}")

# Multiple yield statements
def my_generator():
    yield "Python"
    yield "Greek"
    yield "Iterator"
for val in my_generator():
    print(val)

# Generators and list() in Python

values = list(my_generator())
print(f"List from generator - {values},\ntype - {type(values)},\nSome fun-{values[::-1]}")


#Python generaator expressions
natural_numbers = (n for n in range(1, 25))
print(list(natural_numbers))

# def infinite():
#     num = 1
#     while True:
#         yield num
#         yield num**2
#         num += 1
#
# for n in infinite():
#     print(n)

# Interview questions!!!!!!

# Create a generator to print multiples of 12
def multiples():
    num = 1
    while num <= 5:

            multiple = num * 12
            yield multiple
            num += 1

for i in multiples():
    print(i)


# Create a generator to print the first five even numbers foolowed by the first six odd numbers

def even_odd():

    for n in range(2, 11, 2):
        yield n

    for n in (1, 11, 2):
        yield n
# Create a generator to print all 26 alphabets in smaller cases using the generator expression

alphabets = list(chr(i) for i in range(97, 123))
print(alphabets)

# Example 1
a = range(6)
print(list(a))

#Example 2
def my_cubic_generator(s):

    for i in range(1, s, 2):
        yield pow(i, 3)


for i in my_cubic_generator(11):
    print(i)
print(list(my_cubic_generator(12)))

# Example 3
# Generator expression
my_generator_00 = (pow(i, 5) for i in range(1, 11, 4))
for i in my_generator_00:
    print(i)

# Yield and next()

def my_generator_another_one(d):
    for i in range(1, d, 5):
        yield i * (i+1)

my_gen = my_generator_another_one(21)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))


# Example 5
# Iterator and iterable object
# iterable objects are not iterators
my_string = "Sakartvelo"
my_string_new = iter(my_string)
for i in my_string_new:
    print(str(i).capitalize())


"""Итераторы - специальные объекты для перебора коллекций
Основная их задача - упростить навигацию по отдельным занчениям
последовательностей или словарей.

Специфика - кажддый шаг - следующий элемент последовательности
Ошибка после перебора всех элементов
Итераторы в цикле for

"""

import sys
numbers = iter(range(1, 1000001))
print(sys.getsizeof(numbers))
numbers1 = range(1, 1000001)
print(sys.getsizeof(numbers1))
# Генераторы - возвращают "ленивые итераторы".
# Ленивые итераторы не хранят свое содержимое в памяти

# Пример 1


def csv_reader(filename):
    for row in open(filename, "r"):
        yield row

# пример 2
# создание бесконечной псоледовательности


def infinite_count():
    num = 0
    while True:
        yield num
        num += 1


# for i in infinite_count():
#     print(i, end=" ")

gen = infinite_count()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# Нахождение палиндромов

# def is_palindrome(num):
#     if num//10 == 0:
#         return False
#     temp = num
#     reversed_num = 0
#
#     while temp != 0:
#         reversed_num = (reversed_num * 10 ) + (temp % 10)
#         temp = temp//10
#
#     if num == reversed_num:
#         return num
#     else:
#         return False
#
#
# for i in infinite_count():
#     pal = is_palindrome(i)
#     if pal:
#         print(pal)

nums_squared_lc = [i ** 2 for i in range(1000)]
print(sys.getsizeof(nums_squared_lc))
nums_squared_gc = (i ** 2 for i in range(10000))
print(sys.getsizeof(nums_squared_gc))