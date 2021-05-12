#check whether we can reach the final element of the given array
#refer problem from here- https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last=len(nums)-1
        first=last-1
        
        while first>=0:
            if nums[first]+first>=last:
                last=first
                first-=1
                
            else:
                first-=1
        return last==0
            
