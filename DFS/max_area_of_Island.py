#refer problem from here https://leetcode.com/problems/max-area-of-island/

#time complexity- O(m*n)
#space- L- max length of the blocks (recurison stack length)

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans=0
        m=len(grid)
        n=len(grid[0])
        
        def findArea(r, c):
            if r<0 or r==m or c<0 or c==n or grid[r][c]==0:
                return 0
            grid[r][c]=0
            return 1+findArea(r, c-1)+findArea(r-1, c)+findArea(r, c+1)+findArea(r+1, c)
            
        
        for i in range(m):
            for j in range(n):
                ans=max(ans, findArea(i, j))
                
        return ans
