#refer the problem from https://leetcode.com/problems/multiply-strings/submissions/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num={'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        def get_int(n):
            result=0
            for i in range(len(n)):
                result+=10**i*(num[n[len(n)-1-i]])
            return result
        return str(get_int(num1)*get_int(num2))
        
