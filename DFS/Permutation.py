#permutation of the given array that is return the list where it contains all the permutaion of the given array 
#eg: given array- [1, 2, 3]
#ans- [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

#this works only for array with distinct elements

def permute(self, nums: List[int]) -> List[List[int]]:
        
        dummy=[]
        result=[]
        size=len(nums)
        
        def dfs(nums, dummy, result):
        
            for i in nums:
                if len(dummy)==size:
                    result.append(dummy)
                    break
                elif i in dummy:
                    continue
                else:
                    dfs(nums, dummy+[i], result)
        dfs(nums, dummy, result)
        return result
