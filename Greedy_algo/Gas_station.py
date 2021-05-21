#get the problem statement from here https://leetcode.com/problems/gas-station/
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank=0
        diffSum=0
        start=0
        n=len(gas)
        
        for i in range(n):
            tank+=gas[i]-cost[i]
            diffSum+=gas[i]-cost[i]
            
            if tank<0:
                start=(i+1)%n
                tank=0
        
        if diffSum<0:
            return -1
        return start
