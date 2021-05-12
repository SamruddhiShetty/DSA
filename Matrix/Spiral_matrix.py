#refer problem from https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowMax, rowMin= len(matrix)-1, 0
        colMax, colMin= len(matrix[0])-1, 0
        size=len(matrix)*len(matrix[0])
        
        i, j=0, 0
        result=[]
        while True:
            if colMin>colMax:
                break
            for j in range(colMin, colMax+1):
                result.append(matrix[i][j])
            rowMin+=1
            if rowMin>rowMax:
                break
            for i in range(rowMin, rowMax+1):
                result.append(matrix[i][j])
            colMax-=1
            if colMin>colMax:
                break
            for j in range(colMax, colMin-1, -1):
                result.append(matrix[i][j])
            rowMax-=1
            if rowMin>rowMax:
                break
            for i in range(rowMax, rowMin-1, -1):
                result.append(matrix[i][j])
            colMin+=1
        return result
