########################################################################################################################
# The Vigenère cipher is a classic cipher originally developed by Italian cryptographer Giovan Battista Bellaso
# and published in 1553. It is named after a later French cryptographer Blaise de Vigenère,
# who had developed a stronger autokey cipher (a cipher that incorporates the message of the text into the key).
#
# The cipher is easy to understand and implement, but survived three centuries of attempts to break it,
# earning it the nickname "le chiffre indéchiffrable" or "the indecipherable cipher."
#
# Assume the key is repeated for the length of the text, character by character.
# Note that some implementations repeat the key over characters only
# if they are part of the alphabet -- this is not the case here.
#
# The shift is derived by applying a Caesar shift to a character
# with the corresponding index of the key in the alphabet.
#
# Write a class that, when given a key and an alphabet, can be used to encode and decode from the cipher.
########################################################################################################################
class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.alphabet = [i for i in alphabet]
        self.alphabet_len = len(self.alphabet)
        self.key = [self.alphabet.index(i) for i in key]
        self.key_len = len(self.key)

    def encode(self, text):
        encoded_list = []
        for pos, letter in enumerate(text):
            if letter in self.alphabet:
                position = self.alphabet.index(letter) + self.key[self.range_loop(pos, self.key_len)]
                encoded_list.append(self.alphabet[self.range_loop(position, self.alphabet_len)])

            else:
                encoded_list.append(letter)

        return ''.join(encoded_list)

    def decode(self, text):
        decoded_list = []
        for pos, letter in enumerate(text):
            if letter in self.alphabet:
                position = self.alphabet.index(letter) - self.key[self.range_loop(pos, self.key_len)]
                decoded_list.append(self.alphabet[self.range_loop(position, self.alphabet_len)])

            else:
                decoded_list.append(letter)

        return ''.join(decoded_list)

    @staticmethod
    def range_loop(pos, ran):
        return pos % ran


if __name__ == '__main__':
    abc = 'abcdefghijklmnopqrstuvwxyz'
    k = 'password'
    c = VigenereCipher(k, abc)

    print(c.encode('codewars'))
    print(c.decode('rovwsoiv'))
