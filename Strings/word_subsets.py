#find the problem statement here-  https://leetcode.com/problems/word-subsets/


from collections import defaultdict
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        result=[]
        bdictionary=defaultdict(lambda:0)
        
        for word in B:
            for letter in word:
                bdictionary[letter]=max(word.count(letter), bdictionary[letter])
                
                
        for word in A:
            if all(bdictionary[letter]<=word.count(letter) for letter in bdictionary):
                result.append(word)
                
        return result
