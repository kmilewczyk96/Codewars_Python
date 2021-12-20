########################################################################################################################
# Move the first letter of each word to the end of it,
# then add "ay" to the end of the word. Leave punctuation marks untouched.
########################################################################################################################
def pig_it(text):
    words = text.split(' ')
    for i, v in enumerate(words):
        if v.isalpha():
            words[i] = v[1::] + v[0] + 'ay'

    return ' '.join(words)


if __name__ == '__main__':
    print(pig_it('Hello there mate ! Hope u have good time !'))
