#refer the same name from leetCode

#the main point here is to find the max height n width of the remaining piece after the horizontal and the vertical cut

def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        m=len(horizontalCuts)
        n=len(verticalCuts)
        maxHeight=max(horizonatalCuts[0], h-horizontalCuts[-1])
        maxWidth=max(verticalCuts[0], w-verticalCuts[-1])
        
        for i in range(1, m):
            maxHeight=max(maxHeight, horizontal[i]-horizontal[i-1])
        for j in range(1, n):
            maxWidth=max(maxWidth, vertical[j]-vertical[j-1])
            
        return (maxWidth*maxHeight)%((10**9)+7)
