
from lib import *
import random


def encrypt(block):
    # data = lib.readFile(filename)
    binaryData = str_to_bits(block)
    # binaryData = "10100110010000010100110010000010100110010000001100111111010"
    X = split_into_x_parts_of_y(binaryData, 4, 16)
    # TODO: fix the return - needs to be 128 but not just a multiple of 8
    # key = int2bits(random.randint(1, pow(2, 128)))
    key = "00000000011001000000000011001000000000010010110000000001100100000000000111110100000000100101100000000010101111000000001100100000"
    subkeys = generate_subkeys(key)
    result = []

    print(hex(int(binaryData, 2)))
    for i in range(8):
    # variable names will follow the fourteen-step method 
    # described in the document
        Z = subkeys[i]
        one = m_mul(X[0], Z[0])
        two = m_sum(X[1], Z[1])
        three = m_sum(X[2], Z[2])
        four = m_mul(X[3], Z[3])
        if i == 7: 
            X = [one, two, three, four]
            break
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

        X = [eleven, thirteen, twelve, fourteen]
        print("Round " + str(i + 1) + " " + hex(int(X[0], 2)) + " " +  hex(int(X[1], 2)) + " " +  hex(int(X[2], 2)) + " " +  hex(int(X[3], 2)) + "\tK " +  hex(int(Z[0], 2))  + " " +  hex(int(Z[1], 2))  + " " +  hex(int(Z[2], 2))  + " " +  hex(int(Z[3], 2))  + " " +  hex(int(Z[4], 2))  + " " +  hex(int(Z[5], 2)))
    return ''.join(X), key





if __name__ == '__main__':

    data = "abcdefgh"

    encrypted_data, private_key = encrypt(data)

    print("Encrypted Data:\t" + hex(int(encrypted_data,2)))
    print("Private Key:\t" + hex(int(private_key, 2)))

