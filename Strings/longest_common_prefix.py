#refer from here https://leetcode.com/problems/longest-common-prefix/submissions/
#runtime= O(n^2)-- worst case

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        
        if len(strs)==1:
            return strs[0]
        
        strs=sorted(strs, key=len)
        dummy=strs[0]
        
        for s in strs[1:]:
            dummy2=""
            for j in range(len(dummy)):
                if s[j]==dummy[j]:
                    dummy2+=dummy[j]
                else:
                    break
                    
            if dummy2:
                dummy=dummy2
            else:
                break
        return dummy2
