import sys
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        #ans = sum(nums[:3])
        mindiff=sys.maxsize
        n=len(nums)
        
        for i in range(n-2):
            l, r=i+1, n-1
            small=nums[i]+nums[l]+nums[l+1]
            big=nums[i]+nums[r]+nums[r-1]
            
            if small>target:
                mindiff=min(mindiff, small - target, key=abs)
            elif big<target:
                mindiff=min(mindiff, big - target, key=abs)
            else:
                while l<r:
                    x=nums[i]+nums[l]+nums[r]
                    if x<target:
                        l+=1
                    elif x>target:
                        r-=1
                    else:
                        return target
                    mindiff=min(mindiff, x-target, key=abs)
        return mindiff+target
