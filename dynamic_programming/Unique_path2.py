#refer q from https://leetcode.com/problems/unique-paths-ii/submissions/
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0
        
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        
        arr=[[0 for i in range(n)] for j in range(m)]
        
        arr[0][0]=1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] or (i==0 and j==0):
                    continue
                if i>0:
                    arr[i][j]+=arr[i-1][j]
                if j>0:
                    arr[i][j]+=arr[i][j-1]
        return arr[i][j]
