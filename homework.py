from random import choices, choice


def main():

    def textgen():

        def alphabet():
            return choice([chr(i) for i in range(ord("a"), ord("z")+1)])

        def letterchoice(letter):
            vowels = 'euioay'
            consonants = 'qwrtpsdfghjklzxcvbnm'


            def r_v():
                return choice(vowels)

            def r_c():
                return choice(consonants)

            if letter == ".":
                return alphabet().upper()
            if letter.lower() in consonants:
                return r_c()
            if letter.lower() in vowels:
                return r_v()
            if letter == " ":
                return alphabet()

        def dot():
            return "."

        def space():
            return " "

        res2 = alphabet().upper()
        yield res2

        res1 = res2
        space_chance = 100//7
        dot_chance = 1
        letter_chance = 100 - space_chance - dot_chance
        count = 0

        try:
            while True:
                count += 1
                res2 = choices([' ', '. ', letterchoice(res2)], weights=[space_chance, dot_chance, letter_chance])[0]

                if res1 == res2 == '. ':
                    raise StopIteration

                yield res2

                res1 = res2

        except StopIteration:
            yield res2
            print(f'\nGenerator has finished, with total of tries: {count + 1}')


    a = textgen()

    while True:
        print(next(a), end='')
        