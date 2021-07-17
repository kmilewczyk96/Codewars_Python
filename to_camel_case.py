########################################################################################################################

# Complete the method/function so that it converts dash/underscore delimited words into camel casing.
# The first word within the output should be capitalized only if the original word was capitalized
# (known as Upper Camel Case, also often referred to as Pascal case).


def to_camel_case(text):
    converted = []
    upperbool = 0
    for i in text:
        if upperbool == 0:
            if i != '-' and i != '_':
                converted.append(i)
            else:
                upperbool = 1
        else:
            converted.append(i.upper())
            upperbool = 0

    return ''.join(converted)


########################################################################################################################
