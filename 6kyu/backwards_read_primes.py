def backwards_prime(start, stop):
    if start % 2 == 0:
        start += 1

    my_list = []

    def is_prime(x):
        for i in range(2, x//2):
            if x % i == 0:
                return False
        return True

    for number in range(start, stop + 1, 2):
        if str(number).startswith(('2', '4', '5', '6', '8')):
            pass
        else:
            if is_prime(number):
                reverse = int(str(number)[::-1])
                if number != reverse:
                    if is_prime(reverse):
                        my_list.append(number)

    return my_list


print(backwards_prime(1, 100000))

