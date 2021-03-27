#some change will be there just know the logic

def activitySelection(matrix):
    matrix=sorted(matrix, key=lambda x:x[0])
    
    res=[]
    res.append(matrix[0])
    count=1
    
    for i in range(1, len(matrix)):
        if matrix[i][0]>=res[-1][1]:
            res.append(matrix[i])
            count+=1
            
    return count
        

if __name__=="__main__":
    m=int(input())
    n=int(input())
    matrix=[]
    for i in range(m):
        a=[]
        for j in range(n):
            a.append(int(input()))
        matrix.append(a)
        
    return activitySelection(matrix)
