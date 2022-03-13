import random, string
print(''.join(random.choice(string.ascii_letters) for _ in range(50)))

# the limit for the extended ASCII Character Set
Max_Limit = 255
random_string = ""
for _ in range(10):
    random_integer = random.randint(0, Max_Limit)
    # Keep appending random characters using chr(x)
    random_string += (chr(random_integer))

print(random_string, len(random_string))

random_string = ''

for _ in range(10):
    random_integer = random.randint(97, 97 + 26 - 1)
    flip_bit = random.randint(0, 1)
    random_integer = random_integer -32 if flip_bit ==1 else random_integer
    random_string += (chr(random_integer))
print(random_string, len(random_string))


def multi_yield():
    yield_str = "This will print the first string"
    yield yield_str
    yield_str = "This will print the second string"
    yield yield_str


multi_obj = multi_yield()
print(next(multi_obj))
print(next(multi_obj))


def is_palindrome(num):
    if num//10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num*10)+(temp%10)
        temp=temp//10

    if num == reversed_num:
        return True
    else:
        return False


def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            i = (yield num)
            if i is not None:
                num = i
            num += 1


pal_gen = infinite_palindromes()
for i in pal_gen:
    digits = len(str(i))
    pal_gen.send(10 ** (digits))
