#rotating n*n matrix by 90 degree anti-clockwise direction

class Solution:
    
    #Function to do transpose of matrix.
    def transpose(self,matrix,n):
        for i in range(n): 
            for j in range(i, n): 
                
                #swapping elements at (i,j) and (j,i).
                
                matrix[i][j] ,matrix[j][i] = matrix[j][i], matrix[i][j] 
                  
       
    #after transposing we swap elements of each column (1st with last, 2nd with 
    #second last) one by one for finding left rotation of matrix by 90 degree.
    def reverseColumns(self,matrix,n):
        for i in range(n): 
            j = 0
            k = n-1
            while j < k: 
                
                #swapping elements in each column.
                matrix[j][i] , matrix[k][i] = matrix[k][i],  matrix[j][i] 
                j += 1
                k -= 1
    
    #Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self,a, n): 
        self.transpose(a,n) 
        self.reverseColumns(a,n) 
