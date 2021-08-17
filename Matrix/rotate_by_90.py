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
        
        
    #OR u can do this its the same logic a little easy to understand
    class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        #here we conduct the transpose in_place
        #at every iteration we start from diagonal element to avoid running over
        #the elements which is swapped already
        N=len(matrix[0])
        for i in range(0, N):
            for j in range(i, N):
                matrix[i][j], matrix[j][i]=matrix[j][i], matrix[i][j]
                
        i=0
        j=N-1
        while i<j:
            for k in range(0, N):
                matrix[k][i], matrix[k][j]=matrix[k][j], matrix[k][i]
                
            i+=1
            j-=1
            
        return
