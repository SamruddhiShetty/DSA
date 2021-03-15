def maxFlips(l):
    flip=0
    dummy=l[0]
    for i in range(1, len(l)):
        if l[i]==dummy:
            if flip==1:
                end=(i-1)
                print("Flip from"+ str(start)+" to "+str(end))
                flip=0
            else:
                continue
        else:
            if flip==0:
                start=i
                flip=1
            else:
                continue
    if i==len(l)-1 and flip==1:
        end=i
        print("Flip from"+ str(start)+" to "+str(end))
    return 
                
    

if __name__=="__main__":
    print("Enter the array")
    l=list(map(int, input().strip().split()))
    maxFlips(l)
