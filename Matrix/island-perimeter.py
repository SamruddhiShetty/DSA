#REFER PROBLEM FROM HERE https://leetcode.com/problems/island-perimeter/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter=0
        rows=len(grid)
        cols=len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    perimeter+=4
                    
                    if i>0 and grid[i-1][j]==1:
                        perimeter-=2
                    if j>0 and grid[i][j-1]==1:
                        perimeter-=2
        return perimeter
        
        
        (OR)
        
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter=0
        rows=len(grid)
        cols=len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        dx=i+x
                        dy=j+y
                        
                        if dx>=rows or dy>=cols or dx<0 or dy<0 or grid[dx][dy]==0:
                            perimeter+=1
        return perimeter
