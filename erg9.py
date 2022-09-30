def pair(lst,t):
    for i in lst:
       tmp = t - i
       if tmp in lst:
            lst.remove(tmp)
            lst.remove(i)

    #print(lst)