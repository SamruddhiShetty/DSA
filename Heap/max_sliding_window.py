from collections import deque
import sys

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue=deque([])
        res=deque([])
        currentMax=-(sys.maxsize-1)
        
        for i in range(k):
            x=nums.pop()
            currentMax=max(currentMax, x)
            queue.appendleft(x)
        res.appendleft(currentMax)
        
        while nums:
            x=nums.pop()
            y=queue.pop()
            queue.appendleft(x)
            if y==currentMax:
                currentMax=max(queue)
            else:
                currentMax=max(currentMax, x)                         
            res.appendleft(currentMax)
            
        return res
      
      
#second solution

        N = len(nums)
        i = j = 0

        max_q = deque()
        max_w = []

        while j < N:
            # Keep track of monotonically "decreasing" max values.
            while max_q and nums[j] > max_q[-1]:
                max_q.pop()

            max_q.append(nums[j])

            # Once expanded to the size of the window k, start recording max values and shifting window.
            if j - i + 1 == k:
                max_w.append(max_q[0])

                # Shifted past the first max, pop it off.
                if max_q[0] == nums[i]:
                    max_q.popleft()

                i += 1

            j += 1

        return max_w
