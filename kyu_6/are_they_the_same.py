########################################################################################################################
# Given two arrays a and b write a function comp(a, b)
# that checks whether the two arrays have the "same" elements,
# with the same multiplicities (the multiplicity of a member is the number of times it appears).
# "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.
########################################################################################################################
def comp(array1, array2):
    for i in array1:
        try:
            array2.remove(i * i)
        except (ValueError, TypeError):
            return False

    if len(array2) == 0:
        return True

    return False
