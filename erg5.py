f = open(input("Give path for Ascii text: "), "r")
fl = str(f.read())


def filehash(fl):
    lst = []
    lst.extend(fl)
    text = list(list_split(lst, 16))

    for i in range(len(text)):
        for j in range(16):
            if text[i][j] == None:
                text[i][j] = 00
            else:
                text[i][j] = ord(text[i][j])

    sum = 0
    sum_list = []
    for i in range(16):
        for j in range(len(text)):
            sum += text[j][i]
        sum_list.append("{:02x}".format(sum % 256)) #doing the modulo 256 and hexadecimal conversion (with two digits) at the same time
        sum = 0

    return(''.join(sum_list))


def list_split(lst, n):  #function to split the file into lists of n indexes
    for x in range(0, len(lst), n):
        group = lst[x: n + x]

        if len(group) < n:
            group = group + \
                [None for y in range(n - len(group))]
        yield group