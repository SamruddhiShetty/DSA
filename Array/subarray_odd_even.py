#max length of subarray with alternate even and odd number
def evenOdd(l):
    flag=None
    maxi=count=1
    for i in range(1, len(l)):
        if (l[i]%2==0 and l[i-1]%2!=0) or (l[i]%2!=0 and l[i-1]%2==0):
            count +=1
        else:
            maxi=max(maxi, count)
            count=1  
        
    maxi=max(maxi, count)
    return maxi
            

if __name__=="__main__":
    print("Enter the array")
    l=list(map(int, input().strip().split()))
    print(evenOdd(l))
