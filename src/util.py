import pprint as pp


def transpose_matrix(matrix):
    """
    Transposes a matrix. Used for printing the 4x4 matrices in the correct order.
    :param matrix: a 4x4 matrix
    :return: transposed matrix
    """
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def matrix_int_to_hex(matrix):
    """
    Converts the Integer values of a matrix to Hexadecimal values
    :param matrix: a 4x4 matrix
    :return: 4x4 matrix with Hexadecimal values
    """
    return [[hex(matrix[i][j]) for j in range(len(matrix))] for i in range(len(matrix[0]))]


def pretty_print_matrix(matrix):
    """
    Prints a matrix, prettily
    :param matrix: a 4x4 matrix
    """
    printer = pp.PrettyPrinter(indent=4)
    t_matrix = transpose_matrix(matrix)
    printer.pprint(t_matrix)


def pretty_print_matrix_hex(matrix):
    """
    Prints a matrix, prettily, in hex!
    :param matrix: a 4x4 matrix
    """
    printer = pp.PrettyPrinter(indent=4)
    t_matrix = transpose_matrix(matrix)
    t_matrix_hex = matrix_int_to_hex(t_matrix)
    printer.pprint(t_matrix_hex)
