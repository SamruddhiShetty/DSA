#time efficiency is O(n^2)
#space=O(1)

def calMaxWater(l):
    res=0
    for i in range(1, len(l)-1):
        lmax=rmax=l[i]
        for j in range(0, i):
            lmax=max(l[j], lmax)
            
        for k in range(i, len(l)):
            rmax=max(l[k], rmax)
            
        res+=(min(lmax, rmax)-l[i])
    return res

if __name__=="__main__":
    print("Enter the array")
    l=list(map(int, input().strip().split()))
    print(calMaxWater(l))
    
    
#time-O(n)
#space-O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<=1:
            return 0
        res=0
        lmax, rmax=[-1]*len(height), [-1]*len(height)
        lmax[0]=height[0]
        rmax[-1]=height[-1]
        for i in range(1, len(height)):
            lmax[i]=max(height[i], lmax[i-1])
        for j in range(len(height)-2, -1, -1):
            rmax[j]=max(height[j], rmax[j+1])
            
        for i in range(1, len(height)):
            res+=min(lmax[i], rmax[i])-height[i]
            
        return res
