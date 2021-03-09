def leftRotationByOne(l):
    for i in range(1, len(l)):
        l[i-1], l[i]=l[i], l[i-1]
    return l

if __name__=="__main__":
    print("Enter the array inputs")
    l=list(map(int, input().strip().split()))
    print(leftRotationByOne(l))
    
    
    
#time complexity theta(n)
