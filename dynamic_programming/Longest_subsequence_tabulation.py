#here this is a top-down approach where we compare each characterc of one element with the characters of the other string

def findLongestSubsequence(s1, s2, dp):
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]

if __name__=="__main__":
    print("Enter the first string")
    s1=input()
    print("Enter the second string")
    s2=input()
    dp=[[0 for i in range(len(s1)+1)] for j in range(len(s2)+1)]
    print(findLongestSubsequence(s1, s2, dp))
    
    #time complexity: theta(m*n)
