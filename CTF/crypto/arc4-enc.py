from arc4 import ARC4
#decrypting the ciphertext encoded in RC4. '0xxD' is the key here
ct=b'\xbc"\xc4\xdb0\xb5\xac\x02c\x06\x1a\xa6\x07Cm9uc=\xc7)p\xb3\xad\xb0X\xf6\xed\xef\x06F\x0c\xfc\x1c\r\x11\xabJ\xa3\xe7'
arc4=ARC4('0xxD')
pt = arc4.decrypt(ct)
print(pt)
