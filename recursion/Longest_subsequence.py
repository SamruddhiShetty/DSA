#exponential in the power of 2
#time complexity is O(2^n)


def LargestCommonSubsequence(s1, s2):
    if len(s1)==0 or len(s2)==0:
        return 0
    if s1[0]==s2[0]:
        return 1+LargestCommonSubsequence(s1[1:], s2[1:])
    else:
        return max(LargestCommonSubsequence(s1[1:], s2), LargestCommonSubsequence(s1, s2[1:]))

if __name__=="__main__":
    print("Enter the first string")
    s1=input()
    print("Enter the second string")
    s2=input()
    print(LargestCommonSubsequence(s1, s2))
