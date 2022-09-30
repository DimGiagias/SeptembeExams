def gargamel(a,b):
    counter = 1
    tmp = 0
    for i in range(a,b+1):
        x = [int(num) for num in str(i)]
        for j in range(len(x)):
            tmp += x[j]**counter
            counter += 1
        if tmp==i:
            #print(tmp)
            return True
        tmp = 0
        counter = 1