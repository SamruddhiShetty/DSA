class Solution:
    def minimumNumberOfSwaps(self,S):
        # code here 
        swap=imbalance=CountO=CountC=0
        
        for i in S:
            if i=='[':
                CountO+=1
                if imbalance>0:
                    swap+=imbalance
                    imbalance-=1
            if i==']':
                CountC+=1
                
                if CountC>CountO:
                    imbalance=(CountC-CountO)
        return swap
                    
