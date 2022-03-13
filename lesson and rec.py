class Fib:

    def __init__(self, nn):
        print("__init__")
        self.__nn = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print('__iter__')
        return self

    def __next__(self):
        print('__next__')
        self.__i += 1
        if self.__i >= self.__nn:
            raise StopIteration
        if self.__i in (1, 2):
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret

class Class:
    def __init__(self, n):
        self.__iter = Fib(n)

    def __iter__(self):
        print('Class iter')
        return self.__iter

# object = Class(8)
#
# for i in object:
#     print(i)

def func(n):
    for i in range(n):
        yield i

# for v in func(5):
#     print(v)

def powerof2(n):
    pow = 1
    for i in range(n):
        yield pow
        pow *= 2

# i = list(powerof2(6))
# print(i)

def Fib(n):
    p = pp = 1
    for i in range(n):
        if i in [0,1]:
            yield 1
        else:
            n = p + pp
            p, pp = pp, n
            yield n

# fibs = list(Fib(3))
#
# print(fibs)




def sum_n(n):
    '''Returns sum of all n preceding numbers'''
    if n == 0:
        return 0
    else:
        return n + sum_n(n - 1)

# print(sum_n(9))

def factorial(n):
    '''Returns factorial of a n number'''
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# print(factorial(5))

def fibonachi(n):
    '''Returns Fibonachi Number at nth position'''
    if n == 0: return 0
    if n == 1: return 1
    else:
        return fibonachi(n - 1) + fibonachi(n - 2)

# print(fibonachi(9))