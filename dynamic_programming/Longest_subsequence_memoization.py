def LargestCommonSubsequence(s1, s2, m, n, memo):
    if memo[m-1][n-1]!=-1:
        return memo[m-1][n-1]
    if m==0 or n==0:
        return 0
    else:
        if s1[m-1]==s2[n-1]:
            print("enter phase1")
            memo[m-1][n-1]=1+LargestCommonSubsequence(s1, s2, m-1, n-1, memo)
        else:
            print("entered phase2")
            memo[m-1][n-1]=max(LargestCommonSubsequence(s1, s2, m-1, n, memo), LargestCommonSubsequence(s1, s2, m, n-1, memo))
    print(memo)
    return memo[m-1][n-1]           

if __name__=="__main__":
    print("Enter the first string")
    s1=input()
    print("Enter the second string")
    s2=input()
    m=len(s1)
    n=len(s2)
    memo=[[-1 for i in range(n)]for j in range(m)]
    print(LargestCommonSubsequence(s1, s2, m, n, memo))
    print(memo[0][0])
    
    
    
#TIME EFFICIENCY=THETA(mn)
