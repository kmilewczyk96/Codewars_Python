########################################################################################################################
# Backwards Read Primes are primes that when read backwards in base 10 (from right to left) are a different prime.
# (This rules out primes which are palindromes.)
#
# Examples:
#   13 17 31 37 71 73 are Backwards Read Primes
#   13 is such because it's prime and read from right to left writes 31 which is prime too. Same for the others.
#
# Task:
#
#   Find all Backwards Read Primes between two positive given numbers (both inclusive),
#   the second one always being greater than or equal to the first one.
#   The resulting array or the resulting string will be ordered following the natural order of the prime numbers.
#
#   backwardsPrime(2, 100) => [13, 17, 31, 37, 71, 73, 79, 97]
#   backwardsPrime(9900, 10000) => [9923, 9931, 9941, 9967]
#   backwardsPrime(501, 599) => []
########################################################################################################################
import math


def is_prime(number: int) -> bool:
    max_div = math.floor(math.sqrt(number))
    for i in range(3, max_div + 1, 2):
        if number % i == 0:
            return False

    return True


def backwards_prime(start, stop):
    result = []

    stop += 1
    if start % 2 == 0:
        start += 1

    for number in range(start, stop, 2):
        number_str = str(number)
        if number_str.startswith(('2', '4', '5', '6', '8')):
            continue

        if number_str == number_str[::-1]:
            continue

        number_rev = int(number_str[::-1])
        if number_rev in result:
            result.append(number)
            continue

        if is_prime(number=number) and is_prime(number=number_rev):
            result.append(number)

    return result


if __name__ == '__main__':
    assert backwards_prime(2, 100) == [13, 17, 31, 37, 71, 73, 79, 97]
    assert backwards_prime(9900, 10000) == [9923, 9931, 9941, 9967]
    assert backwards_prime(501, 599) == []
