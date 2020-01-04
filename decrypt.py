
from lib import *
import random


def decrypt(block, key):
    # data = lib.readFile(filename)
    binaryData = str_to_bits(block)
    X = split_into_x_parts_of_y(binaryData, 4, 16)
    # TODO: fix the return - needs to be 128 but not just a multiple of 8
    pre_subkeys = generate_subkeys(key)
    subkeys = generate_decrypt_keys(pre_subkeys)
    result = []

    for i in range(8):
    # variable names will follow the fourteen-step method 
    # described in the document
        Z = subkeys[i]

        one = m_mul(X[0], Z[0])
        two = m_sum(X[1], Z[1])
        three = m_sum(X[2], Z[2])
        four = m_mul(X[3], Z[3])
        five = XOR(one, three)
        six = XOR(two, four)
        seven = m_mul(five, Z[4])
        eight = m_sum(six, seven)
        nine = m_mul(eight, Z[5])
        ten = m_sum(seven, nine)
        eleven = XOR(one, nine)
        twelve = XOR(three, nine)
        thirteen = XOR(two, ten)
        fourteen = XOR(four, ten)

        X = [eleven, thirteen, twelve, fourteen] if i < 8 else [one, two, three, four]

    return ''.join(X)





if __name__ == '__main__':

    originaldata="00010100110010000010100110010000010100110010000001100111111010"
    encrypteddata="1111001110000100111110101100111111011101010111001000010011110001"
    key = "00000000011001000000000011001000000000010010110000000001100100000000000111110100000000100101100000000010101111000000001100100000"



    result = decrypt(encrypteddata, key)
    print("result = " + result)
    print("original = " + originaldata)

