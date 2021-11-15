t1 = [2,4,6,8]
t2 = [3,6,10,12,14]
t3 = [2,4,6,8,3,6,10,12,14]


def concatenation(t1, t2):
    n = len(t1)+len(t2)
    t3 = [0]*n
    for i in range (len(t1)):
        t3[i] = t1[i]
    for i in range (len(t2)):
        t3[len(t1)+i]=t2[i]
    return t3
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                                                                                                                                        