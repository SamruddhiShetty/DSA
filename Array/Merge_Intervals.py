class Solution:
    def getItem(self, ele):
        return ele[0]
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<2:
            return intervals
        mergeList=[]
        a=sorted(intervals, key=self.getItem)
        
        mergeList.append(a[0])
        
        for i in range(1, len(a)):
            if a[i][0]>mergeList[-1][1]:
                mergeList.append(a[i])
            else:
                mergeList[-1][1]=max(mergeList[-1][1], a[i][1])
                
        return mergeList
