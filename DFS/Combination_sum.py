#the problem wants us to find the subset whoes sum is equal to the given target
#from leetcode

#here the problem is solved by using dfs technique DP can also be used but since we are asked to print the subsets DP takes high runtime

#here dfs bcz each time we iterate through the numbers of the given array we check all the possibilities using that number to achieve the target sum.
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res=[]
        resli=[]   #this is a dummy list which maintains the combinations during the iteration 
        
        def dfs(cand, res, resli, target):
            
            for x,i in enumerate(cand):
                if i>target:
                    break
                elif i==target:  #only if we enter this portion the combination is appended to the actual result
                    res.append(resli)
                    res[-1].append(i)
                else:   #here we only check different possibilities if they break in between by entering the first "if" condition then the list of combination till then is lost 
                    dfs(cand[x:], res, resli+[i], target-i)
        dfs(candidates, res, resli, target)
        return res
