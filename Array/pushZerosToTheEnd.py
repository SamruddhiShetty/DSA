#easier solution

def pushZero2(l):
    count=0   #counts number of non-zero numbers
    for i in range(0, len(l)):
        if l[i]!=0:
            l[i], l[count]= l[count], l[i]
            count+=1
    return l


def pushZeros(l):
    res=0
    for i in range(0, len(l)):
        if l[i]==0 and l[res]!=0:
            res=i
        elif l[i]!=0:
            if l[res]==0:
                l[res], l[i]=l[i], l[res]
                res +=1
            else:
                continue
        else:
            continue
            
    return 

if __name__=="__main__":
    print("Enter the array")
    l=list(map(int, input().strip().split()))
    print(pushZeros(l))
