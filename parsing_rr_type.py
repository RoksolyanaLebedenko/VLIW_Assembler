from read_file import read_file

def convert_to_binary(num):
    """
    Method converts number into binary.
    """
    return '{0:05b}'.format(num)


def parsing_rr_type(file_name):
    commands_3operands = dict([("add", "00010101 00001"), ("addi", "10010110"), ("sub", "00010101 00010"), ("subi", "10110110"),
                               ("mul", "00010101 00011"), ("muli", "11110110"), ("div", "00010101"), ("divi", "11100110"),
                               ("and", "00010101 00101"), ("or", "00010101 01000"), ("xor", "00010101 00110"),
                               ("nand", "00010101 00111")])
    #lines = read_file(file_name)
    lines = [('mul', 4, 2, 2), ('mul', 5, 1, 3), ('muli', 5, 5, 4), ('sub', 7, 4, 5), ('divi', 10, 7, 2), ('sub', 8, 8, 8)]
    print(lines)
    parsing = [0]*len(lines)
    for i in range(len(lines)):
        if len(commands_3operands[lines[i][0]]) > 8:
            parsing[i] = commands_3operands[lines[i][0]][:8] + convert_to_binary(lines[i][1]) + \
                         convert_to_binary(lines[i][2]) + convert_to_binary(lines[i][3]) + \
                         commands_3operands[lines[i][0]][9:] + "0000"
        else:
            parsing[i] = commands_3operands[lines[i][0]][:8] + convert_to_binary(lines[i][1]) + \
                         convert_to_binary(lines[i][2]) + "0000000" + convert_to_binary(lines[i][3]) + "10"

    print(parsing)
    return parsing



parsing_rr_type("data.txt")


