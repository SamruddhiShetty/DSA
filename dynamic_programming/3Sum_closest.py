import sys
sys.setrecursionlimit(int(1e5))

class Solution:
    def fun(self, nums, index, sel, current, target, n):
        if sel==3:
            return current
        if  index==n:
            return float('inf')
        if (index, sel, current) in self.dict:
            return self.dict[(index, sel, current)]
        ans1=self.fun(nums, index+1, sel+1, current+nums[index], target, n)
        ans2=self.fun(nums, index+1, sel, current, target, n)
        diff1=abs(target-ans1)
        diff2=abs(target-ans2)
        if diff1<diff2:
            ans=ans1
        else:
            ans=ans2
        self.dict[(index, sel, current)]=ans
        print(self.dict)
        return self.dict[(index, sel, current)]
            
        
        
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        if n==3:
            return sum(nums)
        self.dict=dict()
        return self.fun(nums, 0, 0, 0, target, n)
