#you are given with the total number of candies-N, the number of candies which can be bought for free with 1 candy-K and the cost of each candies.

def candyStore(candies,N,K):
        # code here
        num=(N//(K+1))
        if (N%(K+1))!=0:
            print("yes")
            num+=1
        y=(num*-1)-1
        candies.sort()
        print("num=", end=" ")
        print(num)
        mini=sum(candies[i] for i in range(num))
        maxi=sum(candies[j] for j in range(-1, y, -1))
        return (mini, maxi)
    
if __name__=="__main__":
    N=int(input())
    K=int(input())
    candies=list(map(int, input().strip().split()))
    print(candyStore(candies, N, K))
