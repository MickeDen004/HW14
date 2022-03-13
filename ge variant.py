from random import choices, choice


def main():

    def textgen():

        def alphabet() -> str:
            return choice('abcdefghijklmnopqrstuvwxyz')  #[chr(i) for i in range(ord('a'), ord('z') + 1)]

        def letterchoice(letter: str) -> str:

            vowels = 'euioay'
            cosonants = 'qwrtplkhgfdszxcvbnmj'

            def random_vowel() -> str:
                return choice(vowels)

            def random_cosonant() -> str:
                return choice(cosonants)

            if letter == '. ': return alphabet().upper()
            if letter.lower() in vowels: return random_cosonant()
            if letter.lower() in cosonants: return random_vowel()
            if letter == ' ': return alphabet()

        def dot():
            return '. '

        def space():
            return ' '

        result2 = alphabet().upper()
        yield result2

        ressult1 = result2

        space_chance = 100 // 7

        dot_chance = 1

        letter_chance = 100 - space_chance - dot_chance

        count = 0

        try:
            while True:

                count += 1

                result2 = choices([' ', '. ', letterchoice(result2)], weights=[space_chance, dot_chance, letter_chance])[0]

                if ressult1 == result2 == '. ': raise StopIteration

                yield result2

                ressult1 = result2

        except StopIteration:
            yield result2
            print(f'\nGenerator has finished, with total of tries: {count + 1}')

    a = textgen()

    while True:
        print(next(a), end='')

if __name__ == '__main__':
    import cProfile, pstats
    profiler = cProfile.Profile()
    profiler.enable()
    try:
        main()
    except StopIteration:
        pass
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('tottime')
    stats.print_stats()