def ReverseArray(l, i, j):
    while i<j:
        l[i], l[j]=l[j], l[i]
        i +=1
        j -=1
        
    return l
    
if __name__=="__main__":
    print("enter the array to be rebversed")
    l=list(map(int, input().strip().split()))
    print(ReverseArray(l, 0, len(l)-1))
