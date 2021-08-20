#refer the problem from here https://leetcode.com/problems/valid-parenthesis-string/

#u need to solve it position wise remember

def checkValidString(self, s: str) -> bool:
        
        stack = []
        starStack = []
        
        for pos, char in enumerate(s):
            
            if char == "(":
                stack.append(pos)
                
            elif char == "*":
                starStack.append(pos)
                
            else:
                if stack:
                    stack.pop(-1)
                elif starStack :
                    starStack.pop(-1)
                else:
                    return False
        

        while stack and starStack:
            openPos = stack.pop(-1)
            starPos = starStack.pop(-1)
            
            if openPos > starPos: #if the current '(' position is greater than '*' position then return false since '*' is playing the role of ')' hence it has to be after '('
                return False
        
        
        return len(stack) == 0
