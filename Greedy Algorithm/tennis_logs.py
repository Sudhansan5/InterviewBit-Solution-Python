class Solution:
    def Solve(self,A,B):
        if B[0]==3:
            return 'No'
        global w,l
        if B[0]==1:
            w=1
            l=2
        else:
            w=2
            l=1
        i=0
        while i < A:
            if B[i] == w or B[i] == l:
                if B[i]==w:
                    l ^= w
                else:
                    w ^= l
            else:
                return 'No'
            i+=1
        return 'Yes'

A=3
B=[2,3,1]
C=Solution()
print(C.Solve(A,B))
