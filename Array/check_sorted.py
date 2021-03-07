def checkSorted(l, start):
    for i in range(1, len(l)):
        if l[start]>l[i]:
            return False
        else:
            start=i
    return True
if __name__=="__main__":
    print("enter the array")
    
    l=list(map(int, input().strip().split()))
    
    print(checkSorted(l, 0))
