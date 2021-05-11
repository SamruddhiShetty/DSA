#the problem is to find the k digits to be removed from the string such that the resulting number the minimum possible after following the process.
#if the final value in the stack is "02" then we will have to return the value as "2".


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        if len(num) == k:
            return "0"     
        stack=[]
        
        #from this for and while loop we eliminate only those elements which in the stack is greater than the element to be added to the stack
        for i in num:
            while stack and stack[-1]>i and k:
                stack.pop()
                k-=1
            stack.append(i)
              
        #through this we make sure that the result is the minimum because in the above procedure only the integers which is greater than the elements towards its right
        #will be eliminated but by doing this we will take the first n-k integers if all the max elements are in the end of the string
        res="".join(stack[:-k] if k else stack).lstrip("0")  #stack[:-k] -> stack[0:len(stack)-k] and lstrip strips all the zeros lying on the left side
        return res if res else "0"
                
