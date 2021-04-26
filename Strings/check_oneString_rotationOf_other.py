class Solution:
    
    #Function to check if two strings are rotations of each other or not.
    def areRotations(self, s1, s2):
        #code here
        if len(s1)!=len(s2):
            return 0
          
         #if their length is the same then we create a temperary string where we concatenate s1 twice
        temp=s1+s1
        
        #this is O(n) method to check whether a given string is a substring of another string
        j=0
        for i in temp:
            if j>(len(s2)-1):
                break
            if i==s2[j]:
                j+=1
            else:
                if j!=0:
                    j=0
                else:
                    pass
                
        if j==len(s2):
            return 1
        else:
            return 0
