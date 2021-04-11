from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        elements=defaultdict(int)
        index=len(formula)-1
        currentElement=""
        count=0
        exp=0
        stack=[]
        
        while index>=0:
            char=formula[index]
            
            if char.isnumeric():
                count+=int(char)*(10**exp)
                exp+=1
            elif char ==')':
                if count==0:
                    count=1
                if stack:
                    count=count*stack[-1]
                stack.append(count)
                count=0
                exp=0
            elif char.islower():
                currentElement = char + currentElement
            elif char.isupper():
                currentElement=char+currentElement
                if count==0:
                    count+=1
                if stack:
                    count=count*stack[-1]
                
                elements[currentElement]+=count
                currentElement=""
                count=0
                exp=0
            else:
                stack.pop()
                
            index-=1
            
        res=[]
            
        for key in elements.keys():
            res.append((key, elements[key]))
        res.sort()
        
        result=""
        for i , j in res:
            if j==1:
                result=result+str(i)
            else:
                result=result+str(i)+str(j)
            
        return result
