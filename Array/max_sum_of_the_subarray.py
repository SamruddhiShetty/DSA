#time= O(n)

def maxSubArray(l):
    ans=l[0]
    maxCurr=l[0]
    for i in range(1, len(l)):
        maxCurr=max(maxCurr+l[i], l[i])
        ans=max(ans, maxCurr)
    
    return ans
        
        

if __name__=="__main__":
    print("Enter the array")
    l=list(map(int, input().strip().split()))
    print(maxSubArray(l))
