#the requirement is same as permutation.py but here the difference is that the array has duplicate elements and the result is expected to contain unique sets
#here we use the backtracking technique this method can also be used for arrays with distinct elements

def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def permutation(i, nums):
            if i>=len(nums):
                res.append(nums)
                return 
            
            for j in range(i, len(nums)):
                if j>i and nums[i]==nums[j]:   #here we avoid exchanging those elemenmts whoes values are the same and their indexes are differnet
                    continue
                nums[i], nums[j]=nums[j], nums[i]
                permutation(i+1, nums.copy())   #list.copy() helps in copying the new version of nums all the time(i.e. after exchange)
                
        nums.sort()
        res=[]
        permutation(0, nums)
        return res
                
