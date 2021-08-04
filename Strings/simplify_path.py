#here the problem is solved using dequeue but it can also be solved using stacks
#runtime= O(N)
#space= O(N)

from collections import deque
class Solution:
    def simplifyPath(self, path: str) -> str:
        Q=deque()
        l=path.split('/')
        result=""
        for i in l:
            if len(Q)!=0 and i=="..":
                Q.pop()
            elif i!="" and i!="." and i!="..":
                Q.append(i)
                
        if len(Q)==0:
            return '/'
        else:
            result+='/'
            while Q:
                result+=Q.popleft()
                result+='/'
            return result[:len(result)-1]
