#refer the problem statement from here https://leetcode.com/problems/minimum-path-sum/submissions/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #dp solution 
        if len(grid)==0 or grid==None:
            return 0
        m=len(grid)
        n=len(grid[0])
        dp=[[0 for i in range(n)] for j in range(m)]
        
        #this is mainly solved wrt reaching that what is the min path that
        #can be followed to reach this paticular block grid[i][j] 
        
        for i in range(m):
            for j in range(n):    #the initialization is integrated here itself
                dp[i][j]+=grid[i][j] #irrespective of the position
                
                if i>0 and j>0:
                    dp[i][j]+=min(dp[i-1][j], dp[i][j-1])
                elif i>0:
                    dp[i][j]+=dp[i-1][j]
                elif j>0:
                    dp[i][j]+=dp[i][j-1]
                    
        return dp[i][j]
    
    #runtime- m*n
    #space- m*n
