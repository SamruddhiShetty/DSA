#finding whether there is a subarray with sum equal to given sum

def equalToSum(l, Sum):
    current_sum=l[0]
    s=0
    for i in range(1, len(l)):
        while current_sum>Sum and s<i-1: #s<i-1 to avoid the chance of bringing the current_sum value to zero
            current_sum-=l[s]
            s+=1
        if current_sum==Sum:
            return True
        else:
            current_sum+=l[i]
    if current_sum==Sum:
        return True
    else:
        return False

if __name__=="__main__":
    print("Enter the array")
    l=list(map(int, input().strip().split()))
    print("Enter the sum vlaue")
    Sum=int(input())
    print(equalToSum(l, Sum))
