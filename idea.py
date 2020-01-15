
#!/usr/bin/python python3

from lib import *
import random
import sys


def idea(block, key, mode):
    binaryData = block
    X = split_into_x_parts_of_y(binaryData, 4, 16)

    Z = generate_subkeys(key)
    if mode == 'd':
        Z = generate_decrypt_keys(Z) 

    #  8 Rounds
    for i in range(8):
    # variable names will follow the fourteen-step method 
    # described in the document
        multiplier = i * 6

        one = m_mul(X[0], Z[multiplier + 0])
        two = m_sum(X[1], Z[multiplier + 1])
        three = m_sum(X[2], Z[multiplier + 2])
        four = m_mul(X[3], Z[multiplier + 3])

        five = XOR(one, three)
        six = XOR(two, four)
        seven = m_mul(five, Z[multiplier + 4])
        eight = m_sum(six, seven)
        nine = m_mul(eight, Z[multiplier + 5])
        ten = m_sum(seven, nine)
        eleven = XOR(one, nine)
        twelve = XOR(three, nine)
        thirteen = XOR(two, ten)
        fourteen = XOR(four, ten)
        if i == 7:
            X = [eleven, thirteen, twelve, fourteen]
        else:
            X = [eleven, twelve, thirteen, fourteen]

    # Output pre-processing (half-round)    
    X[0] = m_mul(X[0], Z[48])
    X[1] = m_sum(X[1], Z[49])
    X[2] = m_sum(X[2], Z[50])
    X[3] = m_mul(X[3], Z[51])
    
    return ''.join(X)





if __name__ == '__main__':
    # =============================
    #     Argument Handling
    # =============================
    args = sys.argv
    if len(args) < 3: 
        Exception("mode, message")
    mode_arg = args[1]
    data = args[2]

    mode = ""
    private_key = ""

    if mode_arg == "-e":
        mode = "e"
        data = str_to_bits(data)
        private_key = int2bits(random.randint(1, pow(2, 128)))
    elif mode_arg == "-d":
        mode = "d"
        private_key = args[3]
    else: 
        Exception("Incorrect parameter")


    # =============================
    #     I.D.E.A
    # =============================
    result = idea(data, private_key, mode)

    # =============================
    #     Display
    # =============================
    if mode == "e":
        print("Key: \t" + private_key)
    else:
        result = decode_binary_string(result)
    
    print("Output:\t" + result)

        

