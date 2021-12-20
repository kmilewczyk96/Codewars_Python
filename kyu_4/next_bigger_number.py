########################################################################################################################
# Create a function that takes a positive integer
# and returns the next bigger number that can be formed by rearranging its digits. For example:
#
#   12 ==> 21
#   513 ==> 531
#   2017 ==> 2071

# nextBigger(num: 12)   // returns 21
# nextBigger(num: 513)  // returns 531
# nextBigger(num: 2017) // returns 2071
# If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):
#
#   9 ==> -1
#   111 ==> -1
#   531 ==> -1

# nextBigger(num: 9)   // returns nil
# nextBigger(num: 111) // returns nil
# nextBigger(num: 531) // returns nil
########################################################################################################################
def next_bigger(n):
    nums = [int(i) for i in str(n)]
    tail = []
    compare = 0
    swap_value = ''

    if nums != sorted(nums, reverse=True):
        for pos, value in enumerate(nums[::-1]):
            if value < compare:
                swap_pos = len(nums) - pos - 1
                tail.append(value)
                tail.sort()

                for i in tail:
                    if i > value:
                        swap_value = str(i)
                        tail.remove(i)
                        break

                start = ''.join([str(i) for i in nums[0: swap_pos]])
                end = ''.join(str(i) for i in sorted(tail))

                return int(start + swap_value + end)

            compare = value
            tail.append(compare)

    return -1


if __name__ == '__main__':
    print(next_bigger(122995))
