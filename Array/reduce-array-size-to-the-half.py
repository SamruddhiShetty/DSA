#refer problem from here https://leetcode.com/problems/reduce-array-size-to-the-half/

from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt=Counter(arr)
        frequencies=sorted(cnt.values())
        
        ans, removed, half=0, 0, len(arr)//2
        
        while removed<half:
            ans+=1
            removed+=frequencies.pop()
            
        return ans
        
