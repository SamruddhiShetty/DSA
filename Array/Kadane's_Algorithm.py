#Largest Sum Contiguous Subarray
#refer question from here https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1#

import sys
class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,a,size):
        ##Your code here
        Sums=[]
        Sums.append(a[0])
        
        #here every element of the Sums array will have the max sum of the contigious
        #subarray so far that is at each element we choose max(only current element
        #or current_element + maxSum so far)
        for i in a[1:]:
            Sums.append(max(i, Sums[-1]+i))
            
        return max(Sums)
      
      
 #time- theta(N)
 #space - theta(N)
