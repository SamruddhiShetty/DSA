def findFib(n):
    arr=[0]*(n+1)
    arr[0]=0
    arr[1]=1
    for i in range(2, n+1):
        arr[i]=arr[i-1]+arr[i-2]
    return arr[n]

if __name__=="__main__":
    print("Enter a value")
    n=int(input())
    print(findFib(n))
    
#time complexity is theta(n)
#space complexity is O(n)

#this is faster compared to memorization but also complex compared to memorization
#DP is not the best solution for fibonnaci 
#there is a solution based on divide and conquer which is logn times 
