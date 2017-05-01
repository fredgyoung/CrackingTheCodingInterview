"""
Implement a function which reverses a string.
"""


def rev_str(astring):

    return astring[::-1]


def rev_str2(astring):

    res = ''

    for i in range(len(astring)):
        res += astring[(len(astring) - 1) - i]

    return res


if __name__ == '__main__':

    string1 = 'qwerty'

    print(rev_str(string1))
    print(rev_str2(string1))
