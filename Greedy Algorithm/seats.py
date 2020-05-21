class Solution:
    def Solve(self,A):
        n=len(A)
        mod=10000003
        pos=[]
        for i in range(n):
            if A[i]=='x':
                pos.append(i)

        m=len(pos)
        mid=m//2
        centre = pos[mid]
        total_jump=0

        for i in range(m):
            start=pos[i]
            end=centre-mid+i
            jump=abs(start-end)
            total_jump += jump

        return total_jump%mod

A = "....x..xx...x.."
B = Solution()
print(B.Solve(A))
