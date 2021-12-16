########################################################################################################################
# Write a function named first_non_repeating_letter that takes a string input,
# and returns the first character that is not repeated anywhere in the string.
#
# For example, if given the input 'stress', the function should return 't',
# since the letter t only occurs once in the string, and occurs first in the string.
#
# As an added challenge, upper- and lowercase letters are considered the same character,
# but the function should return the correct case for the initial letter.
# For example, the input 'sTreSS' should return 'T'.
#
# If a string contains all repeating characters, it should return an empty string ("").
########################################################################################################################
def first_non_repeating_letter(string):
    str_ = string.lower()
    cache = []

    for i in str_:
        if i not in cache:
            if str_.count(i) == 1:
                return i if i in string else i.upper()
            cache.append(i)

    return ''


if __name__ == '__main__':
    print(first_non_repeating_letter('sTreSS'))
