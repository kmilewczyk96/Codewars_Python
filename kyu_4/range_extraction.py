########################################################################################################################
# A format for expressing an ordered list of integers is to use a comma separated list of either:

#     - individual integers
#     - or a range of integers denoted by the starting integer separated from the end integer in the range by a dash,
#       '-'. The range includes all integers in the interval including both endpoints.
#       It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
#
# Complete the solution so that it takes a list of integers in increasing order
# and returns a correctly formatted string in the range format.
########################################################################################################################
def solution(args):
    start = 0
    chain = 1
    result = ''
    for pos, val in enumerate(args):
        try:
            # try to check if next argument exists
            next_ = args[pos + 1]
            if val + 1 == next_:
                chain += 1
            else:
                if chain >= 3:
                    result += f'{args[start]}-{val},'
                    start = pos + 1
                elif chain == 2:
                    result += f'{args[pos - 1]},{val},'
                    start = pos + 1
                else:
                    result += f'{val},'
                    start = pos + 1
                chain = 1

        except IndexError:
            # handles for loop ending
            if chain >= 3:
                result += f'{args[start]}-{val}'
            elif chain == 2:
                result += f'{args[pos - 1]},{val}'
                start = pos + 1
            else:
                result += f'{val}'

    return result


if __name__ == '__main__':
    print(solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]))
    print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
    print(solution([-1, 0, 1]))
    print(solution([0]))
