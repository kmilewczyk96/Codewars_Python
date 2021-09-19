def valid(a):
    pairs_count = len(a[0])
    group_length = len(a[0][0])
    print(group_length)

    for pairs in a:
        if len(pairs) != pairs_count:
            return False

    for pairs in a:
        for i in range(0, pairs_count):
            if len(pairs[i]) != group_length:
                return False

    
    return True


if __name__ == '__main__':
    print(
        valid([
            ["AB", "CD"],
            ["AD", "BC"],
            ["BD", "AC"]]
        )
    )

    print(
        valid([
            ["AB", "CD"],
            ["BC"],
            ["BD", "AC"]]
        )
    )
