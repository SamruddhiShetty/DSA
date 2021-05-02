#Given a value V, if we want to make a change for V Rs, and we have an infinite supply of each of the denominations in Indian currency, i.e., 
#we have an infinite supply of { 1, 2, 5, 10, 20, 50, 100, 500, 1000} valued coins/notes, what is the minimum number of coins and/or notes needed to make the change

# Note that this wont work to all the test cases the best solutions is dp solution

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
