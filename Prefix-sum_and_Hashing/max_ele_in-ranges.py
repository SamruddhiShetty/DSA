def findMaxOccur(l, r, arr):
    n=len(l)
    for i in range(0, n):
        arr[l[i]]+=1
        arr[r[i]+1]-=1
    Sum=0
    arr1=[]
    for i in range(0, len(arr)):
        Sum+=arr[i]
        arr[i]=Sum
    x=arr.index(max(arr))
    print(x)
    return
        


if __name__=="__main__":
    print("Enter the start index of ranges")
    l=list(map(int, input().strip().split()))
    print("Enter the end index of ranges")
    r=list(map(int, input().strip().split()))
    #considering the max range to be 1000
    arr=[0]*1000
    findMaxOccur(l, r, arr)
