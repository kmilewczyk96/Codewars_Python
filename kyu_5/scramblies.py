########################################################################################################################
# Complete the function scramble(str1, str2) that returns true
# if a portion of str1 characters can be rearranged to match str2, otherwise returns false.
#
# Notes:
#
# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered
# Input strings s1 and s2 are null terminated.
# Examples
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False
########################################################################################################################
from collections import Counter


def scramble(s1, s2):
    available = Counter(s1)
    available.subtract(s2)
    check_list = available.values()
    for value in check_list:
        if value < 0:
            return False

    return True


if __name__ == '__main__':
    print(scramble('oneplustwo', 'nest'))
    print(scramble('rkqodlw', 'world'))
    print(scramble('cedewaraaossoqqyt', 'codewars'))
    print(scramble('katas', 'steak'))
