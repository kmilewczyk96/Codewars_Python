########################################################################################################################
# Build a function sumNestedNumbers/sum_nested_numbers
# that finds the sum of all numbers in a series of nested arrays raised
# to the power of their respective nesting levels.
# Numbers in the outermost array should be raised to the power of 1.
########################################################################################################################
def sum_nested_numbers(arr, power=1):
    result = []
    for i in arr:
        if isinstance(i, list):
            result.append(sum_nested_numbers(i, power+1))
        else:
            result.append(i ** power)

    return sum(result)


if __name__ == '__main__':
    print(sum_nested_numbers([1, 2, 3, 4, 5]),
          sum_nested_numbers([1, [2], 3, [4, [5]]]),
          sep='\n')
