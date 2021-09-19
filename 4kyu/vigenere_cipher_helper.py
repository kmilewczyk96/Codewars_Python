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

