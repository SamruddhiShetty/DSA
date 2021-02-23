def TowerOfHanoi(n, A, B, C):
    if n==1:
        print("Move 1 from "+ A+ " to "+C )
        return 
    TowerOfHanoi(n-1, A, C, B)
    print("Move", end=" ")
    print(n, end=" ")
    print("from", end=" ")
    print(A+ " to "+ C)
    TowerOfHanoi(n-1, B, A, C)

if __name__=="__main__":
    print("Enter the number of disks")
    n=int(input())
    TowerOfHanoi(n, 'A', 'B', 'C')
    
    #number of movements is 2^n - 1
