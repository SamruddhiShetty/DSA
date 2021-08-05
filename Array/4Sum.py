#refer the problem from here https://leetcode.com/problems/4sum/submissions/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        nums.sort()
        n = len(nums)
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                start = j + 1
                end = n - 1
                while start < end:
                    Sum=nums[i]+nums[j]+nums[start]+nums[end]
                    if Sum == target and [nums[i], nums[j], nums[start], nums[end]] not in result:
                        result.append([nums[i], nums[j], nums[start], nums[end]])
                        start += 1
                        end -= 1
                        while start<end and nums[start]==nums[start-1]:
                            start+=1
                        while start<end and nums[end]==nums[end+1]:
                            end-=1
                    elif Sum < target:
                        start += 1
                    else:
                        end -= 1
                
        return result
                        
