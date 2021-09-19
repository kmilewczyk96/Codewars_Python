def comp(array1, array2):
    for i in array1:
        try:
            array2.remove(i * i)
        except (ValueError, TypeError):
            return False

    if len(array2) == 0:
        return True

    return False
