########################################################################################################################
# Task
#
# Some students decided to go for a walk in the park.
# There they saw a squirrel, which climbed a tree in a spiral at a constant angle to the ground.
# They calculated that in one loop the squirrel climbs h meters (vertical height),
# the height of the tree is equal to H (v in Ruby), and the length of its circumference equals S.
#
# Code Limit:
#   Less than 52 characters
# Other:
#   The result should be rounded to 4 decimal places.
# Examples:
#   For h = 4, H = 16, S = 3, the output should be 20.
#   For h = 8, H = 9, S = 37, the output should be 42.5869.
########################################################################################################################
squirrel=lambda h,H,S:round((h**2+S**2)**.5*H/h,4)


if __name__ == '__main__':
    assert squirrel(4, 16, 3) == 20
    assert squirrel(8, 9, 37) == 42.5869
