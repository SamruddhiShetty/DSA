#Given a set of N jobs where each job i has a deadline and profit associated to it. Each job takes 1 unit of time to complete and only 
#one job can be scheduled at a time. We earn the profit if and only if the job is completed by its deadline. The task is to find the maximum profit 
#and the number of jobs done.

Note: Jobs will be given in the form (Job id, Deadline, Profit) associated to that Job.

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        
        # code here
        jobList=sorted(Jobs, key=lambda x:x.profit, reverse=True)
        
        slot=[False]*n
        
        Profit=count=0

        for i in range(n):
            
            #alloting the time slot such that the time alotted is less than the given deadline
            for j in range(min(n, jobList[i].deadline)-1, -1, -1):
                
                if not slot[j]:
                    slot[j]=True
                    count+=1
                    Profit+=jobList[i].profit
                    break
                    
        return count, Profit
