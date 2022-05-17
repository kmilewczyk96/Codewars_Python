########################################################################################################################
# We want to create a function that will add numbers together when called in succession.
#   add(1)(2) # equals 3
# We also want to be able to continue to add numbers to our chain.
#   add(1)(2)(3) # 6
#   add(1)(2)(3)(4); # 10
#   add(1)(2)(3)(4)(5) # 15
########################################################################################################################
class SomeClass(int):
    def __call__(self, n):
        return SomeClass(self + n)


def add(n):
    return SomeClass(n)


if __name__ == '__main__':
    print(add(1))
    print(add(1)(2))
    print(add(1)(2)(3))
