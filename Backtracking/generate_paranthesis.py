#refer the problem from here https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generate(self, Open, Close, st, result, n):
        if len(st)==n*2:
            result.append(st)
            return
        if Open<n:
            self.generate(Open+1, Close, st+'(', result, n)
            
        if Close<Open:
            self.generate(Open, Close+1, st+')', result, n)
            
    
    def generateParenthesis(self, n: int) -> List[str]:
        Open=0
        Close=0
        result=[]
        self.generate(Open, Close, "", result, n)
        return result
