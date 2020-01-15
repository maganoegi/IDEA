# IDEA
## International Data Encryption Algorithm Implementation
* Symmetric Block Cypher
* Block size: 64 bit
* Key size: 128 bit

## Limitations
I did not aim to make the script user-friendly, but rather to code this algorithm as fast as I can. The code works on blocks of 64 bits - with additional functionalities of file-opening and decomposing into blocks, one could make this into a full encryption/decryption program.

The driver file is __idea.py__ and the code definitions are contained in __lib.py__.

## Encoding [ -e ]
With a 64 bit word: lalaland, we use the command:
```bash
python3 idea.py -e lalaland
```

which yields: 
```bash
Key: 	11001100101010000110110010010101110101010111100100011001011111101110110010000011001101010010101100000110011011101001001100111100

Output:	1111100001010110011001011100101000000101110010000100010001011110
```    

## Decoding [ -d ]
Same format as encoding, but with an additional argument: the key:
```bash
python3 idea.py -d <encoding output> <encoding key>
```
Decoding result:
```bash
Output: lalaland
```
