class Solution:
    def Solve(self,A):
        n=len(A)
        l=[0 for _ in range(n)]
        r=[0 for _ in range(n)]
        for i in range(1,n):
            l[i] = max(l[i-1],A[i-1])

        for i in reversed(range(n-1)):
            r[i] = max(r[i+1],A[i+1])

        ans = 0
        for i in range(n):
            tmp = min(l[i],r[i]) - A[i]
            if tmp < 0:
                continue
            ans += tmp

        return ans
if __name__ == '__main__':
    A=[1,2]
    B=Solution()
    print(B.Solve(A))
