########################################################################################################################
# Write two functions that convert a roman numeral to and from an integer value.
# Multiple roman numeral values will be tested for each function.
# Modern Roman numerals are written by expressing each digit separately starting with the left most digit
# and skipping any digit with a value of zero.
# Input range : 1 <= n < 4000
# In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").
########################################################################################################################
class RomanNumerals:
    @staticmethod
    def to_roman(val: int) -> str:
        result = []
        roman_pairs = (('I', 'V'), ('X', 'L'), ('C', 'D'), ('M',))
        for pos, digit in enumerate(str(val)[::-1]):
            number = int(digit)
            if not number:
                continue
            if number in range(1, 4):
                result.append(number * roman_pairs[pos][0])
            elif number == 4:
                result.append(roman_pairs[pos][0] + roman_pairs[pos][1])
            elif number == 5:
                result.append(roman_pairs[pos][1])
            elif number in range(6, 9):
                result.append(roman_pairs[pos][1] + (number - 5) * roman_pairs[pos][0])
            elif number == 9:
                result.append(roman_pairs[pos][0] + roman_pairs[pos + 1][0])

        result.reverse()
        return ''.join(result)

    @staticmethod
    def from_roman(roman_num: str) -> int:
        sum_ = 0
        trans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        for i in range(len(roman_num) - 1):
            first, second = roman_num[i], roman_num[i + 1]
            if trans[first] < trans[second]:
                sum_ -= trans[first]
            else:
                sum_ += trans[first]

        return sum_ + trans[roman_num[-1]]


if __name__ == '__main__':
    helper = RomanNumerals()
    assert helper.from_roman(roman_num='IV') == 4
    assert helper.from_roman(roman_num='MMM') == 3000
    assert helper.to_roman(val=134) == 'CXXXIV'
    assert helper.to_roman(val=2455) == 'MMCDLV'

