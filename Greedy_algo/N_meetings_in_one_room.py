#given two arrays with start and time of the meet return the maximum number of meet that can be conducted where in we can 
#have only one meet at a time and the end time and the beginning time of another meet should not be equal

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        timing=[]
        for i in range(n):
            timing.append((start[i], end[i]))
            
        timing.sort(key=lambda x:x[1])
        
        current=timing[0][1]
        count=1
        for i in range(1, n):
            if timing[i][0]<=current:
                continue
            else:
                count+=1
                current=timing[i][1]
        return count
