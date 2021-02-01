import numpy as np


def hill_2 (key, plain):
    """
    takes key as 2x2 matrix , plaintext, returns cipher text
    """
    cipher = ""
    is_upper = 0

    if(plain.isupper()):
        is_upper = 1
        plain = plain.lower()

    if(len(plain) %2 !=0):
        plain += 'x'

    p = np.zeros((2,1), dtype=int)
    c = np.zeros((2,1), dtype=int)

    for i in range(0, len(plain), 2):
        p[0] = ord(plain[i]) - 97
        p[1] = ord(plain[i+1]) - 97
        c = np.dot(key, p)
        c[0] = c[0] % 26
        c[1] = c[1] % 26
        cipher += chr(c[0,0] + 97)
        cipher += chr(c[1,0] + 97)

    if(is_upper):
        cipher = cipher.upper()

    return cipher

def hill_3 (key, plain):
    """
    takes key as 3x3 matrix , plaintext, returns cipher text
    """
    cipher = ""
    is_upper = 0

    if(plain.isupper()):
        is_upper = 1
        plain = plain.lower()

    while(len(plain) %3 !=0):
        plain += 'x'

    p = np.zeros((3,1), dtype=int)
    c = np.zeros((3,1), dtype=int)

    for i in range(0, len(plain), 3):
        p[0] = ord(plain[i]) - 97
        p[1] = ord(plain[i+1]) - 97
        p[2] = ord(plain[i+2]) - 97
        c = np.dot(key, p) % 26
        cipher += chr(c[0,0] + 97)
        cipher += chr(c[1,0] + 97)
        cipher += chr(c[2, 0] + 97)

    if(is_upper):
        cipher = cipher.upper()

    return cipher




if __name__ == '__main__':
    key = [[2,4,12], [9,1,6], [7,5,3]]
    plain ="YGREBGHZ"
    print(hill_3(key, plain))