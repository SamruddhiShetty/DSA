#refer the problem from here https://practice.geeksforgeeks.org/problems/choose-and-swap0531/1#

class Solution:
    def chooseandswap (self, A):
        # code here
        position=[-1 for i in range(26)]  #predefinig an array where characters are 
        char1, char2="", ""              #refered by their ord()-97 value(a=97)
        
        
        for i, j in enumerate(A):   #assign the index of those characters in A-string
            if position[ord(j)-97]==-1:
                position[ord(j)-97]=i
            else:
                pass
                
        for r, i in enumerate(A): #here we have to check the first set of character
            n=ord(i)-97         #where i should find the first leftmost character 
            for j in range(n):   #which has a smaller character after it(refer hint)
                if position[j]>r:
                    char1=chr(j+97)
                    char2=i
                    break
            if char1 and char2:
                break
        if not char1 and not char2:
            return A
            
        B=list(A)
        for i in range(len(B)):
            if B[i]==char1:
                B[i]=char2
            elif B[i]==char2:
                B[i]=char1
                
        A=("").join(B)
        return A
