#refer the problem from here https://leetcode.com/problems/3sum/submissions/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:              
        if len(nums)<3:
            return []
        result=[]
        nums.sort()
        i=len(nums)-1
        
        while i>=0:
            if i<len(nums)-1 and nums[i]==nums[i+1]: #avoiding duplicates
                i-=1
            start, end=0, i-1
            while start<end:
                Sum=nums[i]+nums[start]+nums[end]
                
                if Sum==0:
                    if ([nums[i], nums[start], nums[end]] not in result):
                        result.append([nums[i], nums[start], nums[end]])
                    start+=1
                    while start<end and nums[start]==nums[start-1]:  #avoiding duplicates i.e avoiding the situation of going through same set of no.s again and again
                        start+=1
                elif Sum>0:
                    end -=1
                else:
                    start +=1
            i-=1
        return result
