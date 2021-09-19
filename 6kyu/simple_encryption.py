########################################################################################################################
#
# Implement a pseudo-encryption algorithm which given a string S
# and an integer N concatenates all the odd-indexed characters of S
# with all the even-indexed characters of S, this process should be repeated N times.
#
# Examples:
#
# encrypt("012345", 1)  =>  "135024"
# encrypt("012345", 2)  =>  "135024"  ->  "304152"
# encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"
#
# encrypt("01234", 1)  =>  "13024"
# encrypt("01234", 2)  =>  "13024"  ->  "32104"
# encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
#
# Together with the encryption function, you should also implement a decryption function which reverses the process.
# If the string S is an empty value or the integer N is not positive, return the first argument without changes.
#
########################################################################################################################


def decrypt(encrypted_text, n):
    while n > 0:
        position = 1
        result = []
        mid = len(encrypted_text) // 2

        for i in encrypted_text[mid::]:
            result.append(i)

        for i in encrypted_text[0:mid]:
            result.insert(position, i)
            position += 2

        encrypted_text = ''.join(result)
        n -= 1

    return encrypted_text


def encrypt(text, n):
    while n > 0:
        odd = []
        even = []
        for i, v in enumerate(text):
            if i % 2 == 0:
                even.append(v)
            else:
                odd.append(v)
        text = ''.join(odd) + ''.join(even)
        n -= 1

    return text


print(encrypt('0123456', 1))
print(decrypt(encrypt('0123456', 1), 1))
