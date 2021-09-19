def snail(snail_map):
    x = len(snail_map) ** 2

    top = 0
    bottom = len(snail_map)
    left = 0
    right = len(snail_map)

    snailed = []

    if snail_map[0]:
        while x != 0:
            # right
            for i in range(left, right):
                snailed.append(snail_map[top].pop(0))
                x -= 1

            top += 1

            # down
            for i in range(top, bottom):
                snailed.append(snail_map[i].pop(-1))
                x -= 1

            right -= 1

            # left
            for i in range(right, left, -1):
                snailed.append(snail_map[bottom - 1].pop(-1))
                x -= 1

            bottom -= 1

            # up
            for i in range(bottom - 1, top - 1, -1):
                snailed.append(snail_map[i].pop(0))
                x -= 1

            left += 1

    return snailed


if __name__ == '__main__':
    print(snail([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]))