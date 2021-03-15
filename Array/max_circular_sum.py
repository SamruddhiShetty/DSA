def NormalSum(l):
    maxi=mini=l[0]
    res1=res2=l[0]
    for i in range(1, len(l)):
        res1=max(res1+l[i], l[i])
        res2=min(res2+l[i], l[i])
        maxi=max(res1, maxi)
        mini=min(res2, mini)
    return maxi, mini
    
    
    


def maxCircularArray(l):
    s1, s2=NormalSum(l)
    if s1<0:
        return s1
    s3=sum(l)-s2
    return max(s1, s3)

if __name__=="__main__":
    print("Enter the array")
    l=list(map(int, input().strip().split()))
    print(maxCircularArray(l))
