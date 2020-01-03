
from lib import *
import random


def encrypt(block):
    # data = lib.readFile(filename)
    binaryData = str_to_bits(block)
    X = split_into_x_parts_of_y(binaryData, 4, 16)
    # TODO: fix the return - needs to be 128 but not just a multiple of 8
    key = int2bits(random.randint(1, pow(2, 128)))
    subkeys = generate_subkeys(key)
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

    return ''.join(X), key





if __name__ == '__main__':

    data = "abcdefgh"

    encrypted_data, private_key = encrypt(data)

    print("Encrypted Data:\t" + str(encrypted_data))
    print("Private Key:\t" + str(private_key))

