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



if __name__ == '__main__':

    # print(prepare_key('pie', 8, 'repeating'))
    # print(prepare_key('aether','mdampuaf', 'auto'))
    # print(veginer('pie', 'mdampuaf', 'repeating'))
    key = input('Enter secret key:')
    mode = input('Enter mode(repeating/auto):')
    # plain ="YGREBGHZ"
    # print(hill_3(key, plain))

    out = []

    f = open("input/Vigenere/vigenere_plain.txt", "r")
    inp = f.read().splitlines()
    for word in inp:
        out.append(veginer(key, word,mode))
    f.close()

    f = open("input/Vigenere/vigenere_plain_out.txt", "w")
    for word in out:
        f.write(word + '\n')
    f.close()