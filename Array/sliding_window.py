#extra space of theta(k)

def maxSum(l, k):
    dummy=[-1]*k
    maxi=0
    for i in range(0, k):
        dummy[i]=l[i]
    print(dummy)
    maxi=max(maxi, sum(dummy))
    for i in range(k, len(l)):
        dummy[i%k]=l[i]
        print(dummy)
        maxi=max(maxi, sum(dummy))
    return maxi


if __name__=="__main__":
    print("Enter the array")
    l=list(map(int, input().strip().split()))
    print("Enter the K vlaue")
    k=int(input())
    print(maxSum(l, k))
    
    
#theta(1) constant space
def maxSum(l, k):
    Sum=sum(l[:k])
    maxi=Sum
    for i in range(k, len(l)):
        Sum=Sum-l[i-k]+l[i]
        maxi=max(maxi, Sum)
    return maxi


if __name__=="__main__":
    print("Enter the array")
    l=list(map(int, input().strip().split()))
    print("Enter the K vlaue")
    k=int(input())
    print(maxSum(l, k))
