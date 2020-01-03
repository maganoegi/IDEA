import binascii

two_sixteen = pow(2, 16)
two_sixteen_plus_1 = two_sixteen + 1
random_max = pow(2, 128)

def readFile(filename):
    with open(filename, 'r') as file:
        return file.read().replace('\n', ' ')


def AND(a, b):
    if len(a) != len(b):
        raise Exception('AND operator unequal sizes between inputs') 

    result = ""
    for i in range(len(a)):
        result += '1' if a[i] == b[i] == '1' else '0'
    
    return result


def XOR(a, b):
    if len(a) != len(b):
        raise Exception('XOR operator unequal sizes between inputs') 

    result = ""
    for i in range(len(a)):
        result += '1' if a[i] != b[i] else '0'
    
    return result


def circular_left_shift(binString, k):
    res = binString
    for i in range(k):
        tmp = res[0]
        res = res[1:] + tmp
    return res


def generate_subkeys(data):
    if len(data) != 128:
        raise Exception('generate keys function requires an input of 128 bits, but received {}'.format(len(data)))
    
    keys = []
    for i in range(9):
        subkeys = split_into_x_parts_of_y(data, 6, 16)
        keys.append(subkeys)
        data = circular_left_shift(data, 25)
    return keys


def split_into_x_parts_of_y(data, x, y):
    res = []
    for i in range(x):
        multiplier = y * i
        start = 0 + multiplier
        stop = y + multiplier
        res.append(data[start:stop])
    return res


def calculate_inv_of_keys(keys):
    pass


def m_multiplication(a, b):
    a = int(a, 2) 
    b = int(b, 2)
    res = (a * b) % two_sixteen_plus_1
    bits = bin(res)[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def m_sum(a, b):
    a = int(a, 2) 
    b = int(b, 2)
    res = (a + b) % two_sixteen
    bits = bin(res)[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def int2bits(val):
    bits = bin(val)[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


# source: https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
def str_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def str_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

# source: https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m