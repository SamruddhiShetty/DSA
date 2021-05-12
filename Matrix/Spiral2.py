#refer the problem from here- https://leetcode.com/problems/spiral-matrix-ii/

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix=[[0 for x in range(n)]for y in range(n)]        
        rowMax, rowMin= n-1, 0
        colMax, colMin= n-1, 0        
        i, j=0, 0
        Count=1
        while True:
            if colMin>colMax:
                break
            for j in range(colMin, colMax+1):
                matrix[i][j]=Count
                Count +=1
            rowMin+=1
            if rowMin>rowMax:
                break
            for i in range(rowMin, rowMax+1):
                matrix[i][j]=Count
                Count+=1
            colMax-=1
            if colMin>colMax:
                break
            for j in range(colMax, colMin-1, -1):
                matrix[i][j]=Count
                Count+=1
            rowMax-=1
            if rowMin>rowMax:
                break
            for i in range(rowMax, rowMin-1, -1):
                matrix[i][j]=Count
                Count+=1
            colMin+=1
        return (matrix)
