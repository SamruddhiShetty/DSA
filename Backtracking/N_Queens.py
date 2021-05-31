class Solution:
    def __init__(self):
        self.res=[]
    def getSolution(self, arr, n):
        dummy=[]
        for i in range(n):
            dummy.append("".join(arr[i]))
            
        return dummy
            
    def isSafe(self, arr, n, row, col):
        
        #here i check for all the blocks above current block in the same column 
        for i in range(row):
            if arr[i][col]=='Q':
                return False
            
        #here I check for left diagonal running upward i.e. row--, col--
        i, j=row-1, col-1
        while i>=0 and j>=0:
            if arr[i][j]=='Q':
                return False
            i-=1
            j-=1
            
        #here I check for right diagonal of the current block upward i.e. row--, col++
        i, j=row-1, col+1
        while i>=0 and j<n:
            if arr[i][j]=='Q':
                return False
            i-=1
            j+=1
        return True
    
    def solve(self, arr, Crow, n):
        #every time i reach the last rows latest succesful position i come here
        if Crow>=n:
            self.res.append(self.getSolution(arr, n))
            return 
        
        #if we cant find solution at the current row after reaching the last column we trace back to the previous row and change the previous rows queen position
        for i in range(n):
            if self.isSafe(arr, n, Crow, i):
                arr[Crow][i]="Q"
                self.solve(arr, Crow+1, n)                
                arr[Crow][i]="."  #this is where we start backtracking
                
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res
        arr=[["." for i in range(n)] for j in range(n)]
        self.solve(arr, 0, n)
        return self.res
        
        
    #run time- 2^N
    
    #optimized solution
    
    class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def genFormattedBoard(pBoard):
            formatted = []
            for row in pBoard:
                formatted.append("".join(row))
            return formatted
        
        def validate(pBoard, pRow, pCol):
            for i in range(n):
                j = 0
                while (j < pCol):
                    if (pBoard[i][j] == 'Q' and 
                        (pRow + j == pCol + i or 
                         pRow + pCol == i + j or 
                         pRow == i)): 
                        return False
                    j += 1
            return True
        
        def dfs(pBoard, pCol):
            if (pCol == n):
                res.append(genFormattedBoard(pBoard))
                return
            
            ## Iterate over Row to check where to keep Q on row
            for i in range(n):
                if validate(pBoard, i, pCol):
                    pBoard[i][pCol] = 'Q'## Choice
                    dfs(pBoard, pCol + 1) # Recurse
                    pBoard[i][pCol] = '.' ## Revert to backtrack
        
        
        res = []
        emptyBoard = [["."]*n for _ in range(n)]
        dfs(emptyBoard , 0)
        
        return res
