
commands_3operands = dict([("add", "00010101"), ("addi", "10010110"), ("sub", "00010101"), ("subi", "10110110"),
                           ("mul", "00010101"), ("muli", "11110110"), ("div", "00010101"), ("divi", "11100110"),
                           ("and", "00010101"), ("or", "00010101"), ("xor", "00010101"), ("nand", "00010101")])

def convert_to_binary(num):
    """
    Method converts number into binary.
    """
    return '{0:05b}'.format(num)


