def findMaxDiff(l):
    maxdiff=l[1]-l[0]
    minVal=l[0]
    
    for i in range(1, len(l)):
        maxdiff=max(maxdiff, l[i]-minVal)
        minVal=min(minVal, l[i])
        print("maxdiff is", end=" ")
        print(maxdiff)
        print("minVal is", end=" ")
        print(minVal)
        
    return maxdiff


if __name__=="__main__":
    print("Enter the array")
    l=list(map(int, input().strip().split()))
    
    print(findMaxDiff(l))
    
    
#time efficiency theta(n)
#space complexity theta(2)
