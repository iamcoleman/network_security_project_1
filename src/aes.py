from copy import copy


"""S-Box used in the SubBytes function"""
s_box = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
)


def bytes_to_matrix(byte_string):
    """Converts a Python bytes string into a 4x4 matrix"""
    return [list(byte_string[i:i + 4]) for i in range(0, len(byte_string), 4)]


def matrix_to_bytes(matrix):
    """Converts a 4x4 matrix into a Python bytes string"""
    return bytes(sum(matrix, []))


def add_key(state_matrix, key_matrix):
    """
    Performs the AddKey operation in AES
    :param state_matrix: the 4x4 state matrix to add the key to
    :param key_matrix: the 4x4 subkey matrix
    :return: the resulting 4x4 matrix
    """
    result = []
    for i in range(4):
        result.append([])
        for j in range(4):
            result[i].append(state_matrix[i][j] ^ key_matrix[i][j])

    return result


def sub_bytes(state_matrix):
    """
    Performs the SubBytes operation in AES
    :param state_matrix: 4x4 state matrix
    :return: the resulting 4x4 matrix
    """
    result = []
    for i in range(4):
        result.append([])
        for j in range(4):
            result[i].append(s_box[state_matrix[i][j]])

    return result


def shift_rows(sm):
    """
    Performs the ShiftRows operation in AES
    :param sm: the 4x4 state matrix
    :return: the resulting 4x4 matrix
    """
    """
        0,0   1,0   2,0   3,0
        0,1   1,1   2,1   3,1
        0,2   1,2   2,2   3,2
        0,3   1,3   2,3   3,3
    """
    r = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    # first row, no shift
    r[0][0], r[1][0], r[2][0], r[3][0] = sm[0][0], sm[1][0], sm[2][0], sm[3][0]
    # second row, one shift
    r[0][1], r[1][1], r[2][1], r[3][1] = sm[1][1], sm[2][1], sm[3][1], sm[0][1]
    # third row, two shifts
    r[0][2], r[1][2], r[2][2], r[3][2] = sm[2][2], sm[3][2], sm[0][2], sm[1][2]
    # fourth row, three shifts
    r[0][3], r[1][3], r[2][3], r[3][3] = sm[3][3], sm[0][3], sm[1][3], sm[2][3]

    return r


def mix_columns(state_matrix):
    """
    The driver function for MixColumns in AES.
    Sends each column of the input state matrix to the 'mix_column' function one at a time.
    :param state_matrix: the 4x4 state matrix
    :return: the resulting 4x4 matrix
    """
    result = [None, None, None, None]
    for i in range(4):
        column = copy(state_matrix[i])
        new_column = mix_column(column)
        result[i] = new_column

    return result


def mix_column(col):
    """
    Performs the multiplication for MixColumns on a single column from the state matrix
    :param col: column from the 4x4 state matrix
    :return: the resulting column after multiplication
    """
    """
        2 3 1 1
        1 2 3 1
        1 1 2 3
        3 1 1 2
    """
    result = [
        multiply_by_2(col[0]) ^ multiply_by_3(col[1]) ^ col[2] ^ col[3],
        col[0] ^ multiply_by_2(col[1]) ^ multiply_by_3(col[2]) ^ col[3],
        col[0] ^ col[1] ^ multiply_by_2(col[2]) ^ multiply_by_3(col[3]),
        multiply_by_3(col[0]) ^ col[1] ^ col[2] ^ multiply_by_2(col[3])
    ]

    return result


def multiply_by_2(val):
    """
    Multiplies the input value by 2 over bytes in GF(2^8)
    :param val: value from one position in the column
    :return: value after multiplying by 2
    """
    s = val << 1
    s &= 0xff
    if (val & 128) != 0:
        s = s ^ 0x1b

    return s


def multiply_by_3(val):
    """
    Multiplies the input value by 3 over bytes in GF(2^8)
    :param val: value from one position in the column
    :return: value after multiplying by 3
    """
    return multiply_by_2(val) ^ val
