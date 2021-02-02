import numpy as np

#ceaser
def ceaser_encrypt(key, word, mode):
    key = int(key)
    is_lower = True
    if(word.isupper()):
        is_lower = False
        word = word.lower()

    res= ''

    for l in word:
        if(l == '\n'):
            continue
        l_ascii = ord(l) - 97
        l_ascii = (l_ascii +key )% 26 + 97
        res+= chr(l_ascii)
    if (is_lower == False):
        res = res.upper()
    return res
#=============================================
#palyfair
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
        if((i == len(plain)-1)):
            res+=plain[i]
            break

        else:
            if(plain[i]!= plain[i+1]):
                res += plain[i]
                res += plain[i+1]
            else:
                res += plain[i] + 'x'
                res += plain[i+1]


    if(len(res) %2 != 0):
        # res += plain[-1]
        res += 'x'
    # print(res)
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

def play_fair(key, plain, mode):
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

#=============================================
#hill
def hill_2 (key, plain, mode):
    """
    takes key as 2x2 matrix , plaintext, returns cipher text
    """
    cipher = ""
    is_upper = False

    if(plain.isupper()):
        is_upper = True
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

def hill_3 (key, plain, mode):
    """
    takes key as 3x3 matrix , plaintext, returns cipher text
    """
    cipher = ""
    is_upper = False

    if(plain.isupper()):
        is_upper = True
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

#=============================================
#vegenir
def prepare_key(key, plain, mode):
    res = ""
    if mode == 'repeating':
        for i in range(len(plain)):
            res+= key[i% len(key)]
    else:
        diff = len(plain) - len(key)
        for i in range(len(key)):
            res+= key[i]

        for i in range(diff):
            res += plain[i]

    return res

def veginer(key, plain, mode):
    """
    takes key, plain , mode returns cipher
    """
    is_lower = True
    if (plain.isupper()):
        is_lower = False
        plain = plain.upper()

    cipher = ""
    key = prepare_key(key, plain, mode)

    for i in range(len(plain)):
        cipher += chr((ord(key[i])-97 + ord(plain[i])-97)%26 +97)

    if (is_lower == False):
        cipher = cipher.upper()
    return cipher

#============================================
#vernam
def vernam(key, plain, mode):
    """
    takes key, plain return cipher
    """
    is_upper = True
    if (plain.islower()):
        is_upper = False
        plain = plain.upper()
    key = key.upper()


    cipher = ""
    k = key

    if len(plain) < len(key):
        k = key[:len(plain)]

    for i in range(len(plain)):
        first = ord(plain[i])
        second =ord(k[i])
        cipher += chr((first-65 + second-65)%26 +65)

    if (is_upper == False):
        cipher = cipher.lower()
    return cipher

#============================================
#helper functions
def read_run_save(infile, outfile, func, key, mode=1):
    """takes input file as a string, outfile as a string, func as a reference to function,
        key as string or int or list, mode as int
        it will run the fucntion and save the output to outfile
    """
    out = []
    f = open(infile +'.txt', "r")
    inp = f.read().splitlines()
    for word in inp:
        out.append(func(key, word, mode))
    f.close()

    f = open(outfile +'.txt', "w")
    for word in out:
        f.write(word + '\n')
    f.close()


def get_hill_key(key, type):
    keys = key.split(' ')
    res =[]
    if(type == 2):
        for i in range(0,len(keys), 2):
            temp = [int(keys[i]), int(keys[i+1])]
            res.append(temp)
    else:
        for i in range(0,len(keys), 3):
            temp = [int(keys[i]), int(keys[i+1]), int(keys[i+2])]
            res.append(temp)
    return res


if __name__ == '__main__':

    names =     ['ceaser', 'playfair', 'hill2', 'hill3', 'veginer', 'vernam']
    funs =     [ceaser_encrypt, play_fair, hill_2, hill_3, veginer, vernam]
    in_files = ["Caesar/caesar_plain", "PlayFair/playfair_plain", "Hill/hill_plain_2x2", "Hill/hill_plain_3x3",
                "Vigenere/vigenere_plain", "Vernam/vernam_plain"]
    out_files = ["Caesar/caesar_out", "PlayFair/playfair_out", "Hill/hill_out_2x2", "Hill/hill_out_3x3",
                "Vigenere/vigenere_out", "Vernam/vernam_out"]

    print('mode(1) Read from text files and output to text files, mode(2) read from console and output to console')
    mode = int(input('Enter mode num:'))

    if(mode == 1):
        cipher_mode = 1
        for i in range(len(funs)):
            name= names[i]
            key = input('Enter ' + name + ' secret key:')

            if(name == 'hill2'):
                key = get_hill_key(key, 2)
            elif(name == 'hill3'):
                key = get_hill_key(key, 3)
            elif(name == 'veginer'):
                cipher_mode = input('Enter cipher mode (auto/repeating):')

            read_run_save(infile='input/'+in_files[i], outfile='input/'+out_files[i], func=funs[i], key=key, mode=cipher_mode)

    else:
        results = []
        cipher_mode = 1
        plain = input('Enter plain text:')
        for i in range(len(funs)):
            name= names[i]
            key = input('Enter ' + name + ' secret key:')

            if(name == 'hill2'):
                key = get_hill_key(key, 2)
            elif(name == 'hill3'):
                key = get_hill_key(key, 3)
            elif(name == 'veginer'):
                cipher_mode = input('Enter cipher mode (auto/repeating):')

            results.append(funs[i](key,plain,cipher_mode))

        #displaying results
        for i in range(len(results)):
            print(names[i]+' cipher: ' + results[i])


    # read_run_save(infile='input/'+in_files[0], outfile='input/'+out_files[0], func=funs[0], key='3')
    # print(get_hill_key('5 17 8 3', 2))
    # print(get_hill_key('2 4 12 9 1 6 7 5 3', 3))
    # print(play_fair('rats', 'hello',0))

    # print(prepare_text('hello'))
    # print(prepare_text('rkesbbra'))
    # print(prepare_text('umtqoejz'))
    # print(prepare_text('ccwobhnb'))
    # print(prepare_text('ymnqicpx'))
    # print(prepare_text('ipmxxpzw'))

    # print(vernam('aethr', 'hello', 0))


