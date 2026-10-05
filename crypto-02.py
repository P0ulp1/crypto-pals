#!/usr/bin/python3

def fixed_xor(s1, s2):
    b1 = bytes.fromhex(s1)
    b2 = bytes.fromhex(s2)
    
    res = bytes(a ^ b for (a, b) in zip(b1, b2))
    return (res)
    
b1 = "1c0111001f010100061a024b53535009181c"
b2 = "686974207468652062756c6c277320657965"

res = fixed_xor(b1, b2)
print(res)