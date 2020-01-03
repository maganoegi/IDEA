
from lib import *
import random


def decrypt(block, key):
    # data = lib.readFile(filename)
    binaryData = str_to_bits(block)
    X = split_into_x_parts_of_y(binaryData, 4, 16)
    # TODO: fix the return - needs to be 128 but not just a multiple of 8
    pre_subkeys = generate_subkeys(key)
    subkeys = calculate_inv_of_keys(pre_subkeys)
    result = []

    for i in range(9):
    # variable names will follow the fourteen-step method 
    # described in the document
        Z = subkeys[i]
        one = m_multiplication(X[0], Z[0])
        two = m_sum(X[1], Z[1])
        three = m_sum(X[2], Z[2])
        four = m_multiplication(X[3], Z[3])
        five = XOR(one, three)
        six = XOR(two, four)
        seven = m_multiplication(five, Z[4])
        eight = m_sum(six, seven)
        nine = m_multiplication(eight, Z[5])
        ten = m_sum(seven, nine)
        eleven = XOR(one, nine)
        twelve = XOR(three, nine)
        thirteen = XOR(two, ten)
        fourteen = XOR(four, ten)

        X = [eleven, thirteen, twelve, fourteen] if i < 8 else [one, two, three, four]

    return ''.join(X)





if __name__ == '__main__':

    data = "1100101110010101110111000001000111110011101010110100000100001000"
    key = "10011011111000101001111111010111010011001001110010000101000101101001001001111010111010010010111000010111101101010101010101101110"

    encrypted_data = decrypt(data)

    print(encrypted_data)

