import aes
import util


"""
Read the plaintext from "../data/plaintext.txt"
"""
with open('../data/plaintext.txt', 'r') as file:
    plaintext = file.read().strip()


"""
Read the subkeys from "../data/subkey_example.txt"
"""
with open('../data/subkey_example.txt', 'r') as file:
    subkeys = file.readlines()

subkeys = [line.strip() for line in subkeys]


"""
Format the plaintext and subkeys into the correct Python types
"""
plaintext_bytes = plaintext.encode('utf-8')
subkey_0_bytes = bytes.fromhex(subkeys[0])
subkey_1_bytes = bytes.fromhex(subkeys[1])
subkey_0_matrix = aes.bytes_to_matrix(subkey_0_bytes)
subkey_1_matrix = aes.bytes_to_matrix(subkey_1_bytes)


"""
Initial AddKey with SubKey0
"""
initial_state = aes.bytes_to_matrix(plaintext_bytes)
add_key_rd0 = aes.add_key(initial_state, subkey_0_matrix)


"""
SubBytes - Round 1
"""
sub_bytes_rd1 = aes.sub_bytes(add_key_rd0)


"""
ShiftRows - Round 1
"""
shift_rows_rd1 = aes.shift_rows(sub_bytes_rd1)


"""
MixColumns - Round 1
"""
mix_columns_rd1 = aes.mix_columns(shift_rows_rd1)


"""
AddKey - Round 1
"""
add_key_rd1 = aes.add_key(mix_columns_rd1, subkey_1_matrix)


"""
Results - Round 1
"""
result_rd1 = aes.matrix_to_bytes(add_key_rd1)


"""
Generate Report
"""
print(f'Plaintext: {plaintext}')
print(f'SubKey0: 0x{subkeys[0]}')
print(f'SubKey1: 0x{subkeys[1]}')

print('\nInitial State:')
util.pretty_print_matrix_hex(initial_state)

print('\nSubKey0:')
util.pretty_print_matrix_hex(subkey_0_matrix)

print('\nAddKey:')
util.pretty_print_matrix_hex(add_key_rd0)

print('\n\nStart of Round 1:')
print('\nSubBytes:')
util.pretty_print_matrix_hex(sub_bytes_rd1)

print('\nShiftRows:')
util.pretty_print_matrix_hex(shift_rows_rd1)

print('\nMixColumns:')
util.pretty_print_matrix_hex(mix_columns_rd1)

print('\nAddKey:')
util.pretty_print_matrix_hex(add_key_rd1)

print('\n\nRound 1 Results:')
print(f'0x{aes.matrix_to_bytes(add_key_rd1).hex()}')

with open('../data/result.txt', 'w') as writer:
    writer.write('Plaintext: ' + plaintext + '\n')
    writer.write('SubKey0: 0x' + subkeys[0] + '\n')
    writer.write('SubKey1: 0x' + subkeys[1] + '\n\n')
    writer.write('Round 1 Results:\n')
    writer.write('0x' + aes.matrix_to_bytes(add_key_rd1).hex())
