########################################################################################################################
# This time we want to write calculations using functions and get the results. Let's have a look at some examples:
#
# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:
#
# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Division should be integer division.
########################################################################################################################
def zero(*operation):
    if operation:
        return solution(0, operation[0])

    return 0


def one(*operation):
    if operation:
        return solution(1, operation[0])

    return 1


def two(*operation):
    if operation:
        return solution(2, operation[0])

    return 2


def three(*operation):
    if operation:
        return solution(3, operation[0])

    return 3


def four(*operation):
    if operation:
        return solution(4, operation[0])

    return 4


def five(*operation):
    if operation:
        return solution(5, operation[0])

    return 5


def six(*operation):
    if operation:
        return solution(6, operation[0])

    return 6


def seven(*operation):
    if operation:
        return solution(7, operation[0])

    return 7


def eight(*operation):
    if operation:
        return solution(8, operation[0])

    return 8


def nine(*operation):
    if operation:
        return solution(9, operation[0])

    return 9


def plus(*i):
    return 'plus', i[0]


def minus(*i):
    return 'minus', i[0]


def times(*i):
    return 'times', i[0]


def divided_by(*i):
    return 'divided_by', i[0]


def solution(x: int, func):
    if func[0] == 'plus':
        return x + func[1]
    if func[0] == 'minus':
        return x - func[1]
    if func[0] == 'times':
        return x * func[1]
    if func[0] == 'divided_by':
        return int(x / func[1])
