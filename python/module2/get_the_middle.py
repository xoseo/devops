from math import floor, ceil


def get_the_middle(word):
    i = (len(word) -1)//2
    return word[i:-i]


print(get_the_middle("t"))
