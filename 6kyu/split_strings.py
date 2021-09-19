########################################################################################################################
# Complete the solution so that it splits the string into pairs of two characters.
# If the string contains an odd number of characters then it should replace
# the missing second character of the final pair with an underscore ('_').
#
# Examples:
#
# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']
########################################################################################################################

def solution(s):
    list_a = [i for i in s[::2]]
    list_b = [i for i in s[1::2]]
    if len(list_a) != len(list_b):
        list_b.append('_')

    return [list_a[i] + list_b[i] for i in range(len(list_a))]


print(solution('checkthisout'))
