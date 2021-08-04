#used recursion
# https://leetcode.com/problems/count-and-say/submissions/

def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        else:
            st=self.countAndSay(n-1)
            if len(st)==1:
                return "1"+st
            else:
                s2=""
                count=1
                dummy=st[0]
                for i in range(len(st)-1):
                    if st[i]==st[i+1]:
                        count+=1
                    else:
                        s2+=str(count)+dummy
                        count=1
                        dummy=st[i+1]
                s2+=str(count)+dummy
                return s2
