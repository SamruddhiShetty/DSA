#refer problem from https://leetcode.com/problems/permutation-sequence/

import math
class Solution:
    def __init__(self):
        self.ans=""
        self.facts=[]
        self.digits=[]
    def getSolution(self, n, k):
            if n==1:
                self.ans+=str(self.digits[0])
                return
                
            index=k//self.facts[n-1]  #index is the no. of blocks so far and factorial gives the size of the block considering the index we are filling in the ans string
            
            if (k%self.facts[n-1]==0):
                index-=1    #taking care of the boundary condition eg: when n=4, k=12
                
            self.ans+=str(self.digits[index])
            
            self.digits.pop(index)
            
            self.getSolution(n-1, k-(self.facts[n-1]*index)) #dont forget to update the k and n value at each step
            
    def getPermutation(self, n: int, k: int) -> str:
        
        for i in range(n):
            self.digits.append(i+1)
            
        for i in range(0, 10):
            self.facts.append(math.factorial(i))     
            
        self.getSolution(n, k)
        return self.ans
