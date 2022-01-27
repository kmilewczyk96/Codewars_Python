########################################################################################################################
# The rgb function is incomplete.
# Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned.
# Valid decimal values for RGB are 0 - 255.
# Any values that fall out of that range must be rounded to the closest valid value.
#
# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
#
# The following are examples of expected output values:
#   rgb(255, 255, 255) # returns FFFFFF
#   rgb(255, 255, 300) # returns FFFFFF
#   rgb(0,0,0) # returns 000000
#   rgb(148, 0, 211) # returns 9400D3
########################################################################################################################
def rgb(r, g, b):
    result = []
    for value in [r, g, b]:
        if value < 0:
            value = 0
        elif value > 255:
            value = 255

        result.append(hex(value)[2:].upper().zfill(2))

    return ''.join(result)


if __name__ == '__main__':
    print(rgb(255, 256, 270),
          rgb(0, 0, 0),
          rgb(148, 0, 211),
          sep='\n')
