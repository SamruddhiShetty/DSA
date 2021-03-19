#time complexity is O(2n-1)+theta(1)
#space complexity is theta(n+1)

def findFib(n):
    memo=[-1]*(n+1)
    
    if memo[n]==-1:
        if n==0 or n==1:
            return n
        else:
            memo[n]=findFib(n-1)+findFib(n-2)
    return memo[n]

if __name__=="__main__":
    print("Enter a value")
    n=int(input())
    print(findFib(n))
