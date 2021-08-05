#refer the problem from here https://leetcode.com/problems/3sum/submissions/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:              
        if len(nums)<3:
            return []
        result=[]
        nums.sort()
        for i in range(len(nums)-1, -1, -1):
            start, end=0, i-1
            while start<end:
                Sum=nums[i]+nums[start]+nums[end]
                
                if Sum==0:
                    if ([nums[i], nums[start], nums[end]] not in result):
                        result.append([nums[i], nums[start], nums[end]])
                    start+=1
                elif Sum>0:
                    end -=1
                else:
                    start +=1
                    
        return result
