def read_file(file_name):
    parsed_lines = []
    with open(file_name, "r") as data_file:
        for line in data_file:
            opcode = line.split()[0]
            operand_1 = line.split('$')[1][:-2]
            operand_2 = line.split(', ')[1][1:]
            test = line.split(', ')[2]
            if test[0] == '$':
                operand_3 = test[1:][:-2]
            else:
                operand_3 = test[:-2]
            line = (opcode, operand_1, operand_2, operand_3)
            parsed_lines.append(line)
            print("OPCODE:", opcode, "OP1:", operand_1, "OP2:",operand_2, 'OP3:', operand_3)
    return parsed_lines
print(read_file("data.txt"))