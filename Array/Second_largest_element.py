def findSecondLargest(l, res, largest):
    for i in range(1, len(l)):
        if l[i]>l[largest]:
            res=l[largest]
            largest=i
        elif l[i]==l[largest]:
            continue
        else:
            if res==-1:
                res=l[i]
            elif l[i]<=l[res]:
                continue
            else:
                res=l[i]
    return res
                

if __name__=="__main__":
    print("enter the array")
    
    l=list(map(int, input().strip().split()))
    
    print(findSecondLargest(l, -1, 0))
