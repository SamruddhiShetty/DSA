#in this problem we are supposed to return the maximum increase we do for each of the building taking care of the fact that it should not exceed the tallest building
#in that row or column (refer the exact problem statement from leetcode

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        rowMaxes=[max(row) for row in grid]
        colMaxes=[max(col) for col in zip(*grid)]  #zip gives the transpose and * is used to sent the multiple elements that is the array.
        
        return sum(min(rowMaxes[r], colMaxes[c])-val for r, row in enumerate(grid) for c, val in enumerate(row)) #take care of the compression here
      
      
      
      (or)
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        result=0
        
        rowMaxes, colMaxes=[], []
        n=len(grid)
        
        for i in range(n):
            dummy=0
            for j in range(n):
                dummy=max(dummy, grid[i][j])
            rowMaxes.append(dummy)
            
        for i in range(n):
            dummy=0
            for j in range(n):
                dummy=max(grid[j][i])
            colMaxes.append(dummy)
            
        for i in range(n):
            for j in range(n):
                result+=min(rowMaxes[i], colMaxes[j])-grid[i][j]
                
        return result
                
        
        
