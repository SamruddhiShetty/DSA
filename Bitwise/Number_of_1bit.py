#anding a number with a number 1 less than itself than we get the least significant 1 flipped to 0

class Solution:
	def setBits(self, N):
		# code here
		count=0
		while N!=0:
		    N=N & N-1
		    count+=1
		return count
