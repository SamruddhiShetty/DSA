#refer problem from here https://leetcode.com/problems/expression-add-operators/
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res=[]
        if not num:
            return res
        
        n=len(num)
        def solve(pos, path):
            #this is at the final character
            if pos == (n-1):
                path+=num[pos]
                if eval(path)==target:
                    res.append(path)
                return
            solve(pos+1, path+num[pos]+"*")
            solve(pos+1, path+num[pos]+"+")
            solve(pos+1, path+num[pos]+"-")
            
            if (path and path[-1] not in ["+", "-", "*"] and num[pos]=='0') or num[pos]!='0':
                solve(pos+1, path+num[pos])
                
        solve(0, "")
        return res
      
#       Runtime is 4^n
