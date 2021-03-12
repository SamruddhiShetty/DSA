#here we can buy and sell a stock multuple times but not simultaneously

#Selling and buying stocks(Naive) Solution
import sys
sys.setrecursionlimit(1500)


def maxProfit(l, start, end):
    
    if end<=start:
        return 0
    profit=0
    for i in range(start, end):
        for j in range(i+1, end):
            if l[j]>l[i]:
                currentProfit=(l[j]-l[i])+maxProfit(l, start, i-1)+maxProfit(l, j+1, end)
                profit=max(profit, currentProfit)
    return profit        
        


if __name__=="__main__":
    print("enter the array of stock price")
    l=list(map(int, input().strip().split()))
    print(maxProfit(l, 0, len(l)))
    
    
 #efficient solution O(N)

def maxProfit(l):
    profit=0
    for i in range(1, len(l)):
        if l[i]>l[i-1]:
            profit +=(l[i]-l[i-1])
    return profit

if __name__=="__main__":
    print("enter the array of stock price")
    l=list(map(int, input().strip().split()))
    print(maxProfit(l))
