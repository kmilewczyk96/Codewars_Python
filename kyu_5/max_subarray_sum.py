########################################################################################################################
# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence
# in an array or list of integers:
#
#   max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
#   should be 6: [4, -1, 2, 1]
#
# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array.
# If the list is made up of only negative numbers, return 0 instead.
# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid subarray.
########################################################################################################################
def max_sequence(arr):
    current = 0
    max_ = 0

    for i in arr:
        current += i
        if current < 0:
            current = 0
            continue

        if current > max_:
            max_ = current

    return max_


if __name__ == '__main__':
    print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
