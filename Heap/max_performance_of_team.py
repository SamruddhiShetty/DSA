#example of min heap
#refer the problem from here

import heapq

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineer=list(zip(efficiency, speed))
        
        engineer.sort(reverse=True)
        speedSum=0
        ans=0
        heap=[]
        
        for e, s in engineer:
            heapq.heappush(heap, s)
            speedSum+=s
            
            if len(heap)>k:
                speedSum-=heapq.heappop(heap)
                
            ans=max(ans, speedSum*e)
            
        return ans%(10**9+7)
      
    # Complexity

#     Time: O(NlogN + NlogK), NlogN for sorting n engineers by decreasing of their efficiency, 
#       NlogK to iterate all engineers, each time need to perform logK for heappush/heappop.
#     Space: O(N + K)
