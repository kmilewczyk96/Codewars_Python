########################################################################################################################
# ROT13 is a simple letter substitution cipher that replaces a letter
# with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.
#
# Create a function that takes a string and returns the string ciphered with Rot13.
# If there are numbers or special characters included in the string, they should be returned as they are.
# Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
#
# Please note that using encode is considered cheating.
########################################################################################################################
def rot13(message):
    encoded_letters = []

    for letter in message:
        if letter.isalpha():
            cipher = ord(letter) + 13
            if letter.islower():
                encoded_letters.append(cipher if cipher in range(97, 123) else cipher - 25)
            else:
                encoded_letters.append(cipher if cipher in range(65, 91) else cipher - 25)
        else:
            encoded_letters.append(ord(letter))

    return ''.join(chr(i) for i in encoded_letters)


if __name__ == '__main__':
    print(rot13('Hello there!'))
