
def vernam(key, plain):
    """
    takes key, plain return cipher
    """
    is_lower = True
    if (plain.isupper()):
        is_lower = False
        plain = plain.upper()
    cipher = ""
    k = key

    if len(plain) < len(key):
        k = key[:len(plain)]

    for i in range(len(plain)):
        first = ord(plain[i])
        second =ord(k[i])
        cipher += chr((first-65 + second-65)%26 +65)

    if (is_lower == False):
        cipher = cipher.upper()
    return cipher


if __name__ == '__main__':

    # print(vernam('SPARTANS', 'PXPTYRFJ'))
    out = []
    key = input('Enter the secret key: ')
    f = open("input/Vernam/vernam_plain.txt", "r")
    inp = f.read().splitlines()
    print(out)
    for word in inp:
        out.append(vernam(key, word))
    f.close()

    f = open("input/Vernam/vernam_plain_out.txt", "w")
    for word in out:
        f.write(word + '\n')
    f.close()