########################################################################################################################
# https://www.codewars.com/kata/5868b2de442e3fb2bb000119
########################################################################################################################
def closest(strng: str) -> list:
    digit_strings = strng.split()
    if not digit_strings:
        return []

    numbers = [int(digit_str) for digit_str in digit_strings]
    weights = [sum([int(digit) for digit in digit_str]) for digit_str in digit_strings]

    max_weight = max(weights)
    min_difference = max_weight

    result_weights = (max_weight, max_weight)
    result_indexes = (0, 0)

    for pos_x, val_x in enumerate(weights[:-1]):
        for pos_y, val_y in enumerate(weights[pos_x + 1:], start=pos_x + 1):
            weight_difference = abs(val_x - val_y)
            if weight_difference > min_difference:
                continue
            elif weight_difference == min_difference and min(result_weights) <= min(val_x, val_y):
                continue
            else:
                min_difference = weight_difference
                result_weights = (val_x, val_y)
                result_indexes = (pos_x, pos_y)

    result = [
        [result_weights[0], result_indexes[0], numbers[result_indexes[0]]],
        [result_weights[1], result_indexes[1], numbers[result_indexes[1]]]
    ]

    sorting_index = 0 if min_difference != 0 else 1
    result.sort(key=lambda x: x[sorting_index])

    return result


if __name__ == '__main__':
    assert closest("103 123 4444 99 2000 ") == [[2, 4, 2000], [4, 0, 103]]
    assert closest("456899 50 11992 176 272293 163 389128 96 290193 85 52") == [[13, 9, 85], [14, 3, 176]]
    assert closest("239382 162 254765 182 485944 134 468751 62 49780 108 54") == [[8, 5, 134], [8, 7, 62]]
    assert closest("241259 154 155206 194 180502 147 300751 200 406683 37 57") == [[10, 1, 154], [10, 9, 37]]
    assert closest("89998 187 126159 175 338292 89 39962 145 394230 167 1") == [[13, 3, 175], [14, 9, 167]]
