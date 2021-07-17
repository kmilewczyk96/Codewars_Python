########################################################################################################################

# The new "Avengers" movie has just been released!
# There are a lot of people at the cinema box office standing in a huge line.
# Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.
# Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.
# Can Vasya sell a ticket to every person and give change if he initially has no money
# and sells the tickets strictly in the order people queue?
# Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment.
# Otherwise return NO.


def tickets(people):
    change = []
    for i in people:
        if i == 25:
            change.append(25)
        if i == 50:
            try:
                change.remove(25)
            except ValueError:
                return "NO"
            change.append(50)

        if i == 100:
            try:
                change.remove(50)
                change.remove(25)
            except ValueError:
                try:
                    change.remove(25)
                    change.remove(25)
                    change.remove(25)
                except ValueError:
                    return "NO"

    return "YES"


print(tickets([25, 25, 50, 100]))

########################################################################################################################
