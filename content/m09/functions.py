def count_words(text):
    words = text.split()
    return len(words)


def is_even(number):
    return number % 2 == 0


def find_longest(names):
    longest = ""
    for name in names:
        if len(name) > len(longest):
            longest = name
    return longest
