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


print(rot13('Hello there!'))
