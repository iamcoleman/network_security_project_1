import pprint as pp


def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def matrix_int_to_hex(matrix):
    return [[hex(matrix[i][j]) for j in range(len(matrix))] for i in range(len(matrix[0]))]


def pretty_print_matrix(matrix):
    printer = pp.PrettyPrinter(indent=4)
    t_matrix = transpose_matrix(matrix)
    printer.pprint(t_matrix)


def pretty_print_matrix_hex(matrix):
    printer = pp.PrettyPrinter(indent=4)
    t_matrix = transpose_matrix(matrix)
    t_matrix_hex = matrix_int_to_hex(t_matrix)
    printer.pprint(t_matrix_hex)
