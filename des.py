def permutation_1(key):
    """takes 64-bit key as int , permuatate it , returns 56-bit key"""
    res = ''
    p1_matrix = [57,49,41,33,25,17,9,
                 1,58,50,42,34,26,18,
                 10,2,59,51,43,35,27,
                 19,11,3,60,52,44,36,
                 63,55,47,39,31,23,15,
                 7,62,54,46,38,30,22,
                 14,6,61,53,45,37,29,
                 21,13,5,28,20,12,4 ]

    for i in range (len(p1_matrix)):
        res += key[p1_matrix[i]-1]

    return res

def permutation_2(key):
    """takes 56-bit key , permuatate it , returns 48-bit key"""
    res = ''
    p2_matrix = [14,    17,   11,    24,     1,    5,
                  3,    28,   15,     6,    21,   10,
                 23,    19,   12,     4,    26,    8,
                 16,     7,   27,    20,    13,    2,
                 41,    52,   31,    37,    47,   55,
                 30,    40,   51,    45,    33,   48,
                 44,    49,   39,    56,    34,  53,
                 46,    42,   50,    36,    29,   32]

    for i in range (len(p2_matrix)):
        res += key[p2_matrix[i] -1]

    return res

def shift_l (s, shift):
    """shift the string s left by shift amount """
    res = s
    chars = s[0:shift]
    res += chars
    res = res[shift:]
    return res

def left_circualar_shift(l, r):
    """takes left and right parts of key, perform 16 round left shift, returns 16 keys 56-bit each"""
    keys = []
    round_shift ={
        1 : 1,
        2 : 1,
        3 : 2,
        4 : 2,
        5 : 2,
        6 : 2,
        7 : 2,
        8 : 2,
        9 : 1,
        10 :2,
        11 :2,
        12 :2,
        13 :2,
        14 :2,
        15 :2,
        16 : 1
    }

    curr_left = l
    curr_right = r

    for i in range(16):
        #left part
        left_new = shift_l(curr_left, round_shift[i+1])
        curr_left = left_new

        #right part
        right_new = shift_l(curr_right, round_shift[i+1])
        curr_right = right_new

        #concatenate left with right
        keys.append(left_new + right_new)

    return keys

def permuatation_box (s, perm_matrix):
    """takes a string s , permuation matrix , returns new permutated string"""
    res = ''
    for i in range(len(perm_matrix)):
        res += s[perm_matrix[i] -1 ]

    return res


def generate_keys(key):
    """takes original 64-bit original key and returns 16 keys 48-bits each """
    keys = []

    #perform permutation-1 which return 56-bit key
    permutated_key1 = permutation_1(key)

    #divide key into left and right
    l = permutated_key1[0:32]
    r = permutated_key1[32:64]

    #16 round left-circular shift
    keys_16 = left_circualar_shift(l, r) #16 keys

    #perform permutation-2 on the 16 keys
    for i in range(16):
        keys.append(permutation_2(keys_16[i]))

    return keys


def initial_permutation(plain):
    """takes 64-bit input plaintext, returns 64-bit output permutated plain"""
    plain_p = ""
    IP = [58, 50, 42, 34, 26, 18, 10, 2,
          60, 52, 44, 36, 28, 20, 12, 4,
          62, 54, 46, 38, 30, 22, 14, 6,
          64, 56, 48, 40, 32, 24, 16, 8,
          57, 49, 41, 33, 25, 17, 9, 1,
          59, 51, 43, 35, 27, 19, 11, 3,
          61, 53, 45, 37, 29, 21, 13, 5,
          63, 55, 47, 39, 31, 23, 15, 7]
    plain_p = permuatation_box(plain, IP)
    return plain_p


def expansion_permutation(message):
    """takes 32-bit message , return permutated 48-bit message"""
    message_p = ""
    EP = [32, 1, 2, 3, 4, 5,
            4, 5, 6, 7, 8, 9,
            8, 9, 10, 11, 12, 13,
            12, 13, 14, 15, 16, 17,
            16, 17, 18, 19, 20, 21,
            20, 21, 22, 23, 24, 25,
            24, 25, 26, 27, 28, 29,
            28, 29, 30, 31, 32, 1]
    message_p = permuatation_box(message, EP)

    return message_p


def s_box(out_xor):
    """takes 48-bit string , returns 32 bit string"""
    res = ''
    SBox = [
        # S1
        [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
         [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
         [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
         [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

        # S2
        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
         [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
         [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
         [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

        # S3
        [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
         [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
         [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
         [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

        # S4
        [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
         [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
         [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
         [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

        # S5
        [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
         [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
         [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
         [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

        # S6
        [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
         [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
         [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
         [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

        # S7
        [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
         [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
         [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
         [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

        # S8
        [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
         [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
         [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
         [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]],
    ]

    #divide the 48-bit message to 8 6-bit messages
    messages = []
    for i in range(0, 48, 6):
        messages.append(out_xor[i:i+6])

    #sub each message with the new one
    for i in range(len(messages)):
        mess = messages[i]
        row = int(mess[0] + mess[-1], 2)
        col = int(mess[1:5], 2)
        res += f'{SBox[i][row][col]:04b}'

    return res


def final_permutation(out_sBox):
    """takes 32 bit , returns 32 bit string"""
    F_PBox = [16, 7, 20, 21, 29, 12, 28, 17,
              1, 15, 23, 26, 5, 18, 31, 10,
              2, 8, 24, 14, 32, 27, 3, 9,
              19, 13, 30, 6, 22, 11, 4, 25]

    res = permuatation_box(out_sBox, F_PBox)

    return res


def des_function(message, key):
    """takes a 32-bit string, key, returns 32-bit string """
    res = ''

    #perform expansion permutation to get 48-bit output
    message_p = expansion_permutation(message)

    #key xor with message_p
    out_xor = f'{int(key,2)^ int(message_p,2):048b}'

    #s-box
    out_sBox = s_box(out_xor)

    #perform final permutation
    res = final_permutation(out_sBox)

    return res


def fp(cipher):
    """ip-1 """
    FP = [40, 8, 48, 16, 56, 24, 64, 32,
          39, 7, 47, 15, 55, 23, 63, 31,
          38, 6, 46, 14, 54, 22, 62, 30,
          37, 5, 45, 13, 53, 21, 61, 29,
          36, 4, 44, 12, 52, 20, 60, 28,
          35, 3, 43, 11, 51, 19, 59, 27,
          34, 2, 42, 10, 50, 18, 58, 26,
          33, 1, 41, 9, 49, 17, 57, 25]
    res = permuatation_box(cipher, FP)
    return res


def one_round_des(key, plain):
    """takes key and plaintext and performs des encryption algo , returns ciphertext"""
    cipher = ""
    keys = generate_keys(key)
    #perform initial permutation on plaintext
    message_p = initial_permutation(plain)
    l_old = message_p[0:32]
    r_old = message_p[32:64]
    l_new = ''
    r_new = ''
    for i in range(16):
        l_new = r_old
        out_f = des_function(r_old, keys[i])  # 32-bit output from des-function
        r_new = f'{int(l_old, 2) ^ int(out_f, 2):032b}'
        r_old = r_new
        l_old = l_new

    cipher = fp(r_new + l_new)

    return cipher


def one_round_decrypt_des(key, cipher):
    """takes key and cipher , return the plaintext"""
    plain = ""
    keys = generate_keys(key)
    keys.reverse()
    # perform initial permutation on plaintext
    message_p = initial_permutation(cipher)
    l_old = message_p[0:32]
    r_old = message_p[32:64]
    l_new = ''
    r_new = ''
    for i in range(16):
        l_new = r_old
        out_f = des_function(r_old, keys[i])  # 32-bit output from des-function
        r_new = f'{int(l_old, 2) ^ int(out_f, 2):032b}'
        r_old = r_new
        l_old = l_new

    plain = fp(r_new + l_new)

    return plain


def multi_round_des(key, plain, num_rounds):
    """takes key and plaintext, num of rounds and performs des encryption algo , returns ciphertext"""
    cipher = ""
    out = plain

    for i in range(num_rounds):
        out = one_round_des(key, out)

    cipher = out
    return cipher


def multi_round_decrypt_des(key, cipher, num_rounds):
    """takes key and cipher, num of rounds and performs des decryption algo , returns plaintext"""
    plain = ""
    out = cipher

    for i in range(num_rounds):
        out = one_round_decrypt_des(key, out)

    plain = out
    return plain



def rem(s):
    res = ''
    for c in s:
        if(c != ' '):
            res+=c
    return res


if __name__ == '__main__':

    mode = int(input('Select which mode you need, Encryption(Enter 1) or Decryption(Enter 2):'))

    if(mode == 1):
        key = int(input('Enter the secret key:'), 16)
        plain = int(input('Enter plain:'), 16)
        num = int(input('Enter num of rounds:'))
        key = f'{key:064b}'
        plain = f'{plain:064b}'
        res = multi_round_des(key, plain, num)
        print('cipher: ' + hex(int(res, 2))[2:])
    else:
        key = int(input('Enter the secret key: '), 16)
        cipher = int(input('Enter plain:'), 16)
        num = int(input('Enter num of rounds:'))
        key = f'{key:064b}'
        cipher = f'{cipher:064b}'
        dec_res = multi_round_decrypt_des(key, cipher, num)
        print('plain: '+ hex(int(dec_res, 2))[2:])

    k = input("press close to exit")


    #testing
    #working : des-function
    # print(s_box('011000010001011110111010100001100110010100100111') == '01011100100000101011010110010111')
    #print(expansion_permutation('11110000101010101111000010101010') =='011110100001010101010101011110100001010101010101')
    # print(f'{int("000110110000001011101111111111000111000001110010", 2) ^ int("011110100001010101010101011110100001010101010101", 2):048b}'
    #       =="011000010001011110111010100001100110010100100111")

    # print(final_permutation('01011100100000101011010110010111')=='00100011010010101010100110111011')

    # print(initial_permutation(rem(' 0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111'))==rem('1100 1100 0000 0000 1100 1100 1111 1111 1111 0000 1010 1010 1111 0000 1010 1010'))