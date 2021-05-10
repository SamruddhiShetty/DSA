#return True or False based on the fact that whether its possible to make the string palindrome by taking out atmost one character

def validPalindrome(self, s: str) -> bool:
        def check(s):
            if s==s[::-1]:  #here i m checking whether the string is palindrome or not by reversing the string and equating it to the original
                return True
            else:
                return False
            
        if check(s):  #this reduces the run time by few seconds if not the while will take care of this case 
            return True
        
        i, j=0, len(s)-1
        
        while i<j:      #this is the greedy approach where as soon as we find that string[i]!=string[j] we check whether removing either of them will make s a palindrome
                        #if both of them gives false its never possible to make this string a palindrome but if one of them is true then it is possible to make it a pald..
            if s[i]!=s[j]:
                return check(s[:i]+s[i+1:]) or check(s[:j]+s[j+1:])
            i+=1
            j-=1
        return True
