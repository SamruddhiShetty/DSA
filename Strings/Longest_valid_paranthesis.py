class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s)==0:
            return 0
        left=right=maxlength=0
        for i in s:
            if i=='(':
                left+=1
            if i==')':
                right+=1
                
            if left==right:
                maxlength=max(maxlength, 2*right)
            if right>left:
                right=left=0
            
        left=right=0
        
        for i in s[::-1]:
            if i=='(':
                left+=1
            if i==')':
                right+=1
            
            if right==left:
                maxlength=max(maxlength, 2*left)
            if left>right:
                right=left=0
                
        return maxlength
      
      #time=O(n)
      #space=O(1)
