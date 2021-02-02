
def init_matrix(key):
    """return 5x5 matrix"""
    matrix = [['#' for j in range(5)] for i in range(5)]
    key_done = False #flag to check if key is used compleltely
    key_idx = 0          #keep track of key
    alpha_idx = 97   #keep track of alphabitical indeces

    key = "".join(dict.fromkeys(key))

    for i in range(5):
        for j in range(5):
            if(key_done == False):
                matrix[i][j] = key[key_idx]
                if(key_idx == len(key) - 1):
                    key_done = True
                key_idx += 1
            else:
                while(chr(alpha_idx) in key):
                    alpha_idx += 1
                if(chr(alpha_idx) == 'j'):
                    alpha_idx += 1
                matrix[i][j] = chr(alpha_idx)
                alpha_idx += 1

    return matrix

def prepare_text(plain):
    """
    takes plain text and prepare it to be encrypted by play_fair function
    """
    res = ""

    for i in range(0, len(plain), 2):
        if(plain[i]!= plain[i+1]):
            res += plain[i]
            res += plain[i+1]
        else:
            res += plain[i] + 'x'
            res += plain[i+1]


    if(len(res) %2 != 0):
        # res += plain[-1]
        res += 'x'

    return res

def get_index (arr , e):
    """
    takes 2d list and returns index of e in arr
    """
    res = [-1,-1]
    #we are using 5x5 matrix
    for i in range(5):
        for j in range(5):
            if(arr[i][j] == e):
                res[0] = i
                res[1] = j
                break
    return res

def play_fair(key, plain):
    """
    takes matrix 5x5 and plain text , returns cipher text
    """
    is_lower = True
    if (plain.isupper()):
        is_lower = False

    cipher = ""
    plainText = prepare_text(plain)
    matrix = init_matrix(key)

    if('j' in plainText):
        plainText = plainText.replace('j', 'i')

    for i in range(0, len(plainText) , 2):
        a = plainText[i]
        b = plainText[i+1]
        fr,fc = get_index(matrix, a) #first letter row,col indeces
        sr,sc = get_index(matrix, b)

        if(fr == sr): #in same row
            cipher += matrix[fr][(fc+1) %5]  # add first char
            cipher += matrix[sr][(sc+1) %5]  # add second char
        elif(fc == sc):
            cipher += matrix[(fr+1) %5][fc]  # add first char
            cipher += matrix[(sr+1) %5][sc]  # add second char
        else:
            cipher += matrix[fr][sc]  # add first char
            cipher += matrix[sr][fc]  # add second char

    if (is_lower == False):
        cipher = cipher.upper()
    return cipher




if __name__ == '__main__':

    out = []
    key = str(input('Enter the secret key: '))
    f = open("input/PlayFair/playfair_plain.txt", "r")
    inp = f.read().splitlines()
    for word in inp:
        out.append(play_fair(key, word))
    f.close()

    f = open("input/playfair/playfair_out.txt", "w")
    for word in out:
        f.write(word + '\n')
    f.close()
    # key = 'rats'
    # x = init_matrix('archangel')
    # print(x)
    #
    # print('rkesbbra')
    # print(prepare_text('ipmxxpzw'))
    # print(play_fair('rats', "rkesbbra"))

