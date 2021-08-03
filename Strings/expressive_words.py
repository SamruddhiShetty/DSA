#refer it from here https://leetcode.com/problems/expressive-words/submissions/
class Solution:
    def sendWord(self, s, words):
        count=0
        for i in words:
            count+=self.check(s, i)
        return count
    
    def check(self, s, x):
        i=0
        j=0
        while i<len(s) and j<len(x):
            counts=1
            while i<len(s)-1 and s[i]==s[i+1]:
                i+=1
                counts+=1
                
            countx=1
            while j<len(x)-1 and x[j]==x[j+1]:
                j+=1
                countx+=1
                
            if s[i]!=x[j]:
                return 0
            i+=1
            j+=1
            if countx>counts:
                return 0
            if countx==counts:
                continue
            if counts<=2:
                return 0
        return 1 if i>=len(s) and j>=len(x) else 0
                
            
    def expressiveWords(self, s: str, words: List[str]) -> int:
        return self.sendWord(s, words)
