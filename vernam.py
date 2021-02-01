
def vernam(key, plain):
    """
    takes key, plain return cipher
    """
    cipher = ""
    k = key

    if len(plain) < len(key):
        k = key[:len(plain)]

    for i in range(len(plain)):
        first = ord(plain[i])
        second =ord(k[i])
        cipher += chr((first-65 + second-65)%26 +65)

    return cipher


if __name__ == '__main__':

    print(vernam('SPARTANS', 'PXPTYRFJ'))