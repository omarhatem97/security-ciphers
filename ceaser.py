def ceaser_encrypt(key, word):
    res= ''
    for l in word:
        if(l == '\n'):
            continue
        l_ascii = ord(l) - 97
        l_ascii = (l_ascii +key )% 26 + 97
        res+= chr(l_ascii)
    print(res)
    return res




if __name__ == '__main__':

    out = []
    key = int(input('Enter the secret key: '))
    f = open("input/Caesar/caesar_plain.txt", "r")
    for word in f:
        out.append(ceaser_encrypt(key, word))
    f.close()

    f = open("input/Caesar/caeser_out.txt", "w")
    for word in out:
        f.write(word+'\n')
    f.close()
