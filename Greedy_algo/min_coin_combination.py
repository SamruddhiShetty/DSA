def getCoin(coins, Sum):
    coins=sorted(coins, reverse=True)
    c=res=0
    print(coins)
    for i in coins:
        if i <=Sum:
            c=Sum//i
            res+=c
            Sum-=(c*i)
        if Sum==0:
            break
            
    return res
            

if __name__=="__main__":
    print("enter the type of coin which can be taken")
    coins=list(map(int, input().strip().split()))
    print("Enter the sum which u need")
    Sum=int(input())
    print(getCoin(coins, Sum))
