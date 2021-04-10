class Solution:
    def __init__(self):
        self.table=[[-1]*1000]*1000
    def knapSack(self,W, wt, val, n):
        '''
        :param W: capacity of knapsack 
        :param wt: list containing weights
        :param val: list containing corresponding values
        :param n: size of lists
        :return: Integer
        '''
        # code here
        if W==0 or n==0:
            return 0
        
        elif table[n][W]!=-1:
            return self.table[n][W]            
        elif wt[n-1]<=W:
            self.table[n][W]=max(val[n-1]+self.knapSack((W-wt[n-1]), wt, val, n-1),
            self.knapSack(W, wt, val, n-1))
            
        else:
            self.table[n][W]=self.knapSack(W, wt, val, n-1)
            
        return self.table[n][W]
