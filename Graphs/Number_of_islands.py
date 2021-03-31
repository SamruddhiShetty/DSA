#count number of islands-check in leetcode
class Solution:
    def dfs(self, grid, i, j):
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]=='0':
            return 0
        grid[i][j]='0'
        self.dfs(grid, i-1, j)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j-1)
        self.dfs(grid, i, j+1)
        return 1
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count=0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j]=='1':
                    count+=self.dfs(grid, i, j)
                else:
                    continue
        return count
