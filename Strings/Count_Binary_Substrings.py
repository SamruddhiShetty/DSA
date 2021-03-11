#first solution is with O(N) time ans O(N) Space
#HERE WE CREATE THE GROUPS STORE IT AND THEN FIND THE MIN OF EACH TWO ELEMENTS
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        group=[]
        current=s[0]
        count=1
        for i in s[1:]:
            if i==current:
                count +=1
            else:
                group.append(count)
                count=1
                current=i
        group.append(count)
        
        ans=0
        z=group[0]
        for j in group[1:]:
            ans +=min(z, j)
            z=j
        return ans



#second is with O(N) time and O(1) space EFFICIENT
#HERE WE DONT STORE BUT WE JUST ADD THE MIN OF FIRST TWO GROUPS WE GET AND MOVE FOREWORD
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev, ans=0, 0
        current=s[0]
        count=1
        for i in s[1:]:
            if i==current:
                count +=1
            else:
                ans +=min(prev, count)
                prev=count
                count=1
                current=i
        ans +=min(prev, count)
        return ans
