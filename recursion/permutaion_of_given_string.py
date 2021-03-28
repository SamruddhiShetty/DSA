class Solution:
    def __init__(self):
        self.res=[]
    def permute(self, L, l, r):
        if l==r:
            self.res.append("".join(x for x in L))
            return
            
        else:
            for i in range(l, r):
                L[i], L[l]=L[l], L[i]
                self.permute(L, l+1, r)
                L[i], L[l]=L[l], L[i] 
            
    def find_permutation(self, S):
        # Code here
        L=list(S)
        l=0
        r=len(S)
        self.permute(L, l, r)
        ans=sorted(self.res)
        return ans


if __name__=='__main__':
    t=int(input())
    for i in range(t):
        S=input()
        ob=Solution()
        ans=ob.find_permutation(S)
        print("hey2")
        for i in ans:
            print(i, end=" ")
        print()
