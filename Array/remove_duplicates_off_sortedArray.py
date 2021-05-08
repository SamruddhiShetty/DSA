#the function is to return the length of the array with only umique elements
#we have to remove the elements in-place with O(1) space
#link to the problem- https://leetcode.com/problems/remove-duplicates-from-sorted-array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=0
        for i in range(1, len(nums)):
            if nums[i]!=nums[n]:
                n+=1
                nums[n]=nums[i]
                
        return n+1
      
      
      (or)
          nums[:]=sorted(set(nums))
          return len(nums)
