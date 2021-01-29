from copy import deepcopy

def convert_to_state(plain):
    """convert plain text to state matrix """
    #init state matrix 4x4
    state = [['#' for j in range(4)] for i in range(4)]
    shift = 0
    for i in range(4):
        for j in range(4):
            state[j][i] = plain[shift] + plain[shift+1]
            shift += 2
    return state


def add_round_key(state, key):
    """takes state matrix , key matrix and xoring them"""
    res = [['#' for j in range(4)] for i in range(4)]
    for i in range(4):
        for j in range(4):
            res[i][j] = f'{int(state[i][j], 16) ^ int(key[i][j], 16):02x}'

    return res


def s_box(out_roundKey):
    """takes state matrix and return new matrix 4x4"""
    res = [['#' for j in range(4)] for i in range(4)]
    sbox = [99, 124, 119, 123, 242, 107, 111, 197, 48, 1, 103, 43, 254, 215, 171, 118, 202, 130, 201, 125, 250, 89, 71,
            240, 173, 212, 162, 175, 156, 164, 114, 192, 183, 253, 147, 38, 54, 63, 247, 204, 52, 165, 229, 241, 113,
            216, 49, 21, 4, 199, 35, 195, 24, 150, 5, 154, 7, 18, 128, 226, 235, 39, 178, 117, 9, 131, 44, 26, 27, 110,
            90, 160, 82, 59, 214, 179, 41, 227, 47, 132, 83, 209, 0, 237, 32, 252, 177, 91, 106, 203, 190, 57, 74, 76,
            88, 207, 208, 239, 170, 251, 67, 77, 51, 133, 69, 249, 2, 127, 80, 60, 159, 168, 81, 163, 64, 143, 146, 157,
            56, 245, 188, 182, 218, 33, 16, 255, 243, 210, 205, 12, 19, 236, 95, 151, 68, 23, 196, 167, 126, 61, 100,
            93, 25, 115, 96, 129, 79, 220, 34, 42, 144, 136, 70, 238, 184, 20, 222, 94, 11, 219, 224, 50, 58, 10, 73, 6,
            36, 92, 194, 211, 172, 98, 145, 149, 228, 121, 231, 200, 55, 109, 141, 213, 78, 169, 108, 86, 244, 234, 101,
            122, 174, 8, 186, 120, 37, 46, 28, 166, 180, 198, 232, 221, 116, 31, 75, 189, 139, 138, 112, 62, 181, 102,
            72, 3, 246, 14, 97, 53, 87, 185, 134, 193, 29, 158, 225, 248, 152, 17, 105, 217, 142, 148, 155, 30, 135,
            233, 206, 85, 40, 223, 140, 161, 137, 13, 191, 230, 66, 104, 65, 153, 45, 15, 176, 84, 187, 22]

    for i in range (4):
        for j in range(4):
            curr = int(out_roundKey[i][j], 16)
            res[i][j] = str(format(sbox[curr], "x"))
    return res




def shift_rows(out_sbox):
    """perform shift rows , takes 4x4 returns 4x4"""
    print(out_sbox)
    res = deepcopy(out_sbox)

    for i in range(4):
        if(i == 0):
            continue
        elif (i == 1):#
            for j in range(4):
                res[i][j] = out_sbox[i][(j+1)%4]

        elif (i == 2):
            res[i][0], res[i][2] = out_sbox[i][2], out_sbox[i][0]
            res[i][1], res[i][3] = out_sbox[i][3], out_sbox[i][1]
        else:
            for j in range(4):
                res[i][(j+1)%4] = out_sbox[i][j]

    return res


def mix_coloumns(state):
    gfp2 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54,
            56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106,
            108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148,
            150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190,
            192, 194, 196, 198, 200, 202, 204, 206, 208, 210, 212, 214, 216, 218, 220, 222, 224, 226, 228, 230, 232,
            234, 236, 238, 240, 242, 244, 246, 248, 250, 252, 254, 27, 25, 31, 29, 19, 17, 23, 21, 11, 9, 15, 13, 3, 1,
            7, 5, 59, 57, 63, 61, 51, 49, 55, 53, 43, 41, 47, 45, 35, 33, 39, 37, 91, 89, 95, 93, 83, 81, 87, 85, 75,
            73, 79, 77, 67, 65, 71, 69, 123, 121, 127, 125, 115, 113, 119, 117, 107, 105, 111, 109, 99, 97, 103, 101,
            155, 153, 159, 157, 147, 145, 151, 149, 139, 137, 143, 141, 131, 129, 135, 133, 187, 185, 191, 189, 179,
            177, 183, 181, 171, 169, 175, 173, 163, 161, 167, 165, 219, 217, 223, 221, 211, 209, 215, 213, 203, 201,
            207, 205, 195, 193, 199, 197, 251, 249, 255, 253, 243, 241, 247, 245, 235, 233, 239, 237, 227, 225, 231,
            229]

    gfp3 = [0, 3, 6, 5, 12, 15, 10, 9, 24, 27, 30, 29, 20, 23, 18, 17, 48, 51, 54, 53, 60, 63, 58, 57, 40, 43, 46, 45,
            36, 39, 34, 33, 96, 99, 102, 101, 108, 111, 106, 105, 120, 123, 126, 125, 116, 119, 114, 113, 80, 83, 86,
            85, 92, 95, 90, 89, 72, 75, 78, 77, 68, 71, 66, 65, 192, 195, 198, 197, 204, 207, 202, 201, 216, 219, 222,
            221, 212, 215, 210, 209, 240, 243, 246, 245, 252, 255, 250, 249, 232, 235, 238, 237, 228, 231, 226, 225,
            160, 163, 166, 165, 172, 175, 170, 169, 184, 187, 190, 189, 180, 183, 178, 177, 144, 147, 150, 149, 156,
            159, 154, 153, 136, 139, 142, 141, 132, 135, 130, 129, 155, 152, 157, 158, 151, 148, 145, 146, 131, 128,
            133, 134, 143, 140, 137, 138, 171, 168, 173, 174, 167, 164, 161, 162, 179, 176, 181, 182, 191, 188, 185,
            186, 251, 248, 253, 254, 247, 244, 241, 242, 227, 224, 229, 230, 239, 236, 233, 234, 203, 200, 205, 206,
            199, 196, 193, 194, 211, 208, 213, 214, 223, 220, 217, 218, 91, 88, 93, 94, 87, 84, 81, 82, 67, 64, 69, 70,
            79, 76, 73, 74, 107, 104, 109, 110, 103, 100, 97, 98, 115, 112, 117, 118, 127, 124, 121, 122, 59, 56, 61,
            62, 55, 52, 49, 50, 35, 32, 37, 38, 47, 44, 41, 42, 11, 8, 13, 14, 7, 4, 1, 2, 19, 16, 21, 22, 31, 28, 25,
            26]
    Nb = len(state)
    n = [word[:] for word in state]

    for i in range(Nb):
        n[i][0] = ((gfp2[state[i][0]] ^ gfp3[state[i][1]]
                   ^ state[i][2] ^ state[i][3]))
        n[i][1] = ((state[i][0] ^ gfp2[state[i][1]]
                   ^ gfp3[state[i][2]] ^ state[i][3]))
        n[i][2] = ((state[i][0] ^ state[i][1]
                   ^ gfp2[state[i][2]] ^ gfp3[state[i][3]]))
        n[i][3] = ((gfp3[state[i][0]] ^ state[i][1]
                   ^ state[i][2] ^ gfp2[state[i][3]]))

    return n


def transpose_matrix(out_mix):
    """returns the transpose of matrix"""
    res = deepcopy(out_mix)
    for i in range(len(out_mix)):
        for j in range(len(out_mix)):
            res[j][i] = out_mix[i][j]
    return res


def get_word(num, key):
    """returns a specific word from a key"""
    return key[num*8 : num*8+8]


def shift8(word):
    """shifts a word by 8 bits"""
    toShift = word[0:2]
    return word[2:] + toShift



def subByte(word):
    """
    returns subByte of word eg: same as s-box..... this function is used in keygeneration
    """
    sbox = [99, 124, 119, 123, 242, 107, 111, 197, 48, 1, 103, 43, 254, 215, 171, 118, 202, 130, 201, 125, 250, 89, 71,
            240, 173, 212, 162, 175, 156, 164, 114, 192, 183, 253, 147, 38, 54, 63, 247, 204, 52, 165, 229, 241, 113,
            216, 49, 21, 4, 199, 35, 195, 24, 150, 5, 154, 7, 18, 128, 226, 235, 39, 178, 117, 9, 131, 44, 26, 27, 110,
            90, 160, 82, 59, 214, 179, 41, 227, 47, 132, 83, 209, 0, 237, 32, 252, 177, 91, 106, 203, 190, 57, 74, 76,
            88, 207, 208, 239, 170, 251, 67, 77, 51, 133, 69, 249, 2, 127, 80, 60, 159, 168, 81, 163, 64, 143, 146, 157,
            56, 245, 188, 182, 218, 33, 16, 255, 243, 210, 205, 12, 19, 236, 95, 151, 68, 23, 196, 167, 126, 61, 100,
            93, 25, 115, 96, 129, 79, 220, 34, 42, 144, 136, 70, 238, 184, 20, 222, 94, 11, 219, 224, 50, 58, 10, 73, 6,
            36, 92, 194, 211, 172, 98, 145, 149, 228, 121, 231, 200, 55, 109, 141, 213, 78, 169, 108, 86, 244, 234, 101,
            122, 174, 8, 186, 120, 37, 46, 28, 166, 180, 198, 232, 221, 116, 31, 75, 189, 139, 138, 112, 62, 181, 102,
            72, 3, 246, 14, 97, 53, 87, 185, 134, 193, 29, 158, 225, 248, 152, 17, 105, 217, 142, 148, 155, 30, 135,
            233, 206, 85, 40, 223, 140, 161, 137, 13, 191, 230, 66, 104, 65, 153, 45, 15, 176, 84, 187, 22]

    res = ''
    for i in range (0,8,2):
        curr = int(word[i]+word[i+1], 16)
        res += f'{sbox[curr]:02x}'
    return res





def generate_keys(key):
    """takes key as a string, returns keys list[k0,k1,....k10]"""

    keys = []
    rcon = [0x01000000, 0x02000000, 0x04000000, 0x08000000, 0x10000000, 0x20000000, 0x40000000, 0x80000000,
            0x1b000000, 0x36000000]

    #append the first key
    keys.append(key)

    for i in range(1, 11):
        currKey = '' #generate each key in string currKey
        words = []
        for j in range(4): #generate words (w0, w1,...w3)
            currword = 0x0 #generate each word in string currword
            if (j==0):
                t1 = get_word(0, keys[i-1]) #get w0 from k[j-1]

                t2 = subByte(shift8(get_word(3,keys[i-1]))) #subByte(k[n-1]: W3 >>8)

                t3 = rcon[i-1]
                currword = f'{int(t1, 16) ^ int(t2, 16) ^ t3:08x}'
            else:
                t1 = get_word(j, keys[i-1])

                t2 = words[j-1]

                currword = f'{int(t1, 16) ^ int(t2, 16):08x}'

            words.append(currword)
            currKey += str(currword)
        keys.append(currKey)

    return keys








def aes(key, plain):
    """takes 32-long plain string , key, returns cipher text"""
    cipher = ''

    #generate 11 keys
    keys = generate_keys(key)

    #convert palain text to state matrix
    state = convert_to_state(plain)

    #add round key
    out_roundKey = add_round_key(state, key)

    #s-box (sub-byte)
    out_sbox = s_box(out_roundKey)

    #shift rows
    out_shift = shift_rows(out_sbox)

    # inverse matrix
    out_inv = transpose_matrix(out_shift)

    #mix coloumns
    out_mix = mix_coloumns(out_inv)



    return cipher


def rem(s):
    res = ''
    for c in s:
        if(c != ' '):
            res+=c
    return res




def list_to_hex(l):
    """takes list of strings change it to hex"""
    res = deepcopy(l)
    for i in range(len(l)):
        for j in range (len(l)):
            res[i][j] = hex(int(l[i][j], 16))
    return res

def list_to_int(l):
    """takes list of strings change it to int"""
    res = deepcopy(l)
    for i in range(len(l)):
        for j in range(len(l)):
            res[i][j] = int(l[i][j], 16)
    return res


if __name__ == '__main__':

    # a = convert_to_state('54776F204F6E65204E696E652054776F')
    # b = convert_to_state(rem('54 68 61 74 73 20 6D 79 20 4B 75 6E 67 20 46 75'))
    # c = (add_round_key(a,b))
    # d = s_box(c)
    # e = shift_rows(d)
    # e = list_to_int(e)
    # e = transpose_matrix(e)
    # print(e)
    # print((mix_coloumns(e)))
    # s=hex(int('54776F204F6E65204E696E652054776F', 16))
    # print(get_word(1,s))
    # print(shift8('af7f6798'))
    # print(subByte('7f6798af'))
    print(generate_keys(rem('54 68 61 74 73 20 6D 79 20 4B 75 6E 67 20 46 75')))