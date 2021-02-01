
def prepare_key(key, plain_len, mode):
    res = ""
    if mode == 'repeating':
        for i in range(plain_len):
            res+= key[i% len(key)]

    return res



def veginer(key, plain, mode):
    """
    takes key, plain , mode returns cipher
    """
    cipher = ""
    key = prepare_key(key, len(plain), mode)

    for i in range(len(plain)):
        cipher += chr((ord(key[i])-97 + ord(plain[i])-97)%26 +97)

    return cipher









if __name__ == '__main__':

    print(prepare_key('pie', 8, 'repeating'))
    print(veginer('pie', 'mdampuaf', 'repeating'))