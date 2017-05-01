"""
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""


def uniq_chars(astring):

    char_list = []

    for char in astring:
        if char in char_list:
            return False
        else:
            char_list.append(char)

    return True


def uniq_chars2(astring):

    for char in astring:
        if astring.count(char) > 1:
            return False

    return True




if __name__ == '__main__':

    string1 = 'abcdefghijklmnopqrstuvwxyz'
    string2 = 'abcdefga'

    print(uniq_chars(string1))
    print(uniq_chars(string2))
    print(uniq_chars2(string1))
    print(uniq_chars2(string2))
