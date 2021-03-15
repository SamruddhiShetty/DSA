#Supposed to find the sum of the subarray given in the function where the start and end index is given in the function.

def preFixedSum(l):
    a=[]
    Sum=0
    for i in range(0, len(l)):
        Sum+=l[i]
        a.append(Sum)
    return a

def getSum(start, end, a):
    if start==0:
        return a[end]
    else:
        return a[end]-a[start-1]

if __name__=="__main__":
    print("Enter the array")
    l=list(map(int, input().strip().split()))
    a=preFixedSum(l)
    print(getSum(3, 6, a))
