def checkShuffle(s1, s2, result):
    if len(result)<(len(s1)+len(s2)):
        return False
    i, j, k=0, 0, 0
    
    while k<len(result):
        if i<len(s1) and s1[i]==result[k]:
            i+=1
        elif j<len(s2) and s2[j]==result[k]:
            j+=1
        else:
            return False
        k+=1
    if i<len(s1) or j<len(s2):
        return False
    else:
        return True
    
if __name__=="__main__":
    s1=input()
    s2=input()
    result=input()
    print(checkShuffle(s1, s2, result))
