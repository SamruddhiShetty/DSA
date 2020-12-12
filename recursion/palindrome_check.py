class Solution:
	def is_palindrome(self, n):
		# Code here
		n=list(map(int, str(n)))
		def check(n, i, j):
		    if len(n)<=1:
		        return True
		    if i>j:
		        return True
		    else:
		        return (n[i]==n[j]) and check(n, i+1, j-1)
		ans=check(n, 0, len(n)-1)
		        
        if ans==True:
            return "Yes"
        else:
            return "No"
