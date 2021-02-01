
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
    cipher = ""
    key = prepare_key(key, plain, mode)

    for i in range(len(plain)):
        cipher += chr((ord(key[i])-97 + ord(plain[i])-97)%26 +97)

    return cipher



if __name__ == '__main__':

    # print(prepare_key('pie', 8, 'repeating'))
    print(prepare_key('aether','mdampuaf', 'auto'))
    print(veginer('pie', 'mdampuaf', 'repeating'))