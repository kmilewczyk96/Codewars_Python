########################################################################################################################
# Create two functions to encode and then decode a string using the Rail Fence Cipher.
# This cipher is used to encode a string by placing each character successively in a diagonal along a set of "rails".
# First start off moving diagonally and down. When you reach the bottom,
# reverse direction and move diagonally and up until you reach the top rail.
# Continue until you reach the end of the string. Each "rail" is then read left to right to derive the encoded string.
#
# For example, the string "WEAREDISCOVEREDFLEEATONCE" could be represented in a three rail system as follows:
#   W       E       C       R       L       T       E
#     E   R   D   S   O   E   E   F   E   A   O   C
#       A       I       V       D       E       N
#
# The encoded string would be:
#   WECRLTEERDSOEEFEAOCAIVDEN
#
# Write a function/method that takes 2 arguments, a string and the number of rails, and returns the ENCODED string.
# Write a second function/method that takes 2 arguments, an encoded string and the number of rails,
# and returns the DECODED string.
#
# For both encoding and decoding, assume number of rails >= 2 and that passing an
# empty string will return an empty string.
#
# Note that the example above excludes the punctuation and spaces just for simplicity.
# There are, however, tests that include punctuation. Don't filter out punctuation as they are a part of the string.
########################################################################################################################
from collections import deque


def encode_rail_fence_cipher(string: str, n: int) -> str:
    step = -1
    current_row = 0
    rows = ['' for _ in range(n)]
    for letter in string:
        rows[current_row] += letter
        if current_row == 0 or current_row == n - 1:
            step *= -1
        current_row += step

    return ''.join(rows)


def decode_rail_fence_cipher(string: str, n: int) -> str:
    if not string:
        return ''
    rows = [deque() for _ in range(n)]
    letter_gen = (letter for letter in string)

    for row in range(n):
        index = row
        rows[row].append(next(letter_gen))
        first_step = (n - 1 - row) * 2
        second_step = row * 2
        while True:
            if first_step:
                index += first_step
                if index > len(string) - 1:
                    break
                rows[row].append(next(letter_gen))

            if second_step:
                index += second_step
                if index > len(string) - 1:
                    break
                rows[row].append(next(letter_gen))

    decoded = ''
    step = -1
    current_row = 0
    while True:
        try:
            decoded += rows[current_row].popleft()
        except IndexError:
            return decoded
        if current_row == 0 or current_row == n - 1:
            step *= -1
        current_row += step


if __name__ == '__main__':
    assert encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 3) == "WECRLTEERDSOEEFEAOCAIVDEN"
    assert encode_rail_fence_cipher("Hello, World!", 4) == "H !e,Wdloollr"
    assert decode_rail_fence_cipher("H !e,Wdloollr", 4) == "Hello, World!"
    assert decode_rail_fence_cipher("WECRLTEERDSOEEFEAOCAIVDEN", 3) == "WEAREDISCOVEREDFLEEATONCE"