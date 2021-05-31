#refer the question from https://leetcode.com/problems/insert-interval/submissions/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        intervals.append(newInterval)
        intervals=sorted(intervals)
        n=len(intervals)
        
        res.append(intervals[0])
        
        for i in range(1, n):
            s, e=intervals[i][0], intervals[i][1]
            pe=res[-1][1]
            
            if pe<s:
                res.append(intervals[i])
            else:
                res[-1][1]=max(pe, e)
                
        return res
           
