########################################################################################################################
# In this Kata you must create a function that takes an amount of US currency in cents,
# and returns a dictionary/hash which shows the least amount of coins used to make up that amount.
# The only coin denominations considered in this exercise are:
#     Pennies (1¢),
#     Nickels (5¢),
#     Dimes (10¢)
#     and Quarters (25¢).
#
# Therefor the dictionary returned should contain exactly 4 key/value pairs.
#
# Notes:
#
# If the function is passed either 0 or a negative number,
# the function should return the dictionary with all values equal to 0.
# If a float is passed into the function, its value should be be rounded down,
# and the resulting dictionary should never contain fractions of a coin.
########################################################################################################################
def loose_change(cents):
    change = {x: 0 for x in ('Nickels', 'Pennies', 'Dimes', 'Quarters')}
    cents = int(cents)

    if cents > 0:
        q = cents // 25
        cents -= q * 25
        change['Quarters'] = q

        d = cents // 10
        cents -= d * 10
        change['Dimes'] = d

        n = cents // 5
        cents -= n * 5
        change['Nickels'] = n

        p = cents // 1
        change['Pennies'] = p

    return change


if __name__ == '__main__':
    print(loose_change(29),
          loose_change(91),
          loose_change(0),
          loose_change(-2),
          loose_change(3.999),
          sep='\n')
