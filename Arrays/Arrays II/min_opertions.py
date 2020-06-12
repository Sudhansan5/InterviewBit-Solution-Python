class Solution:
    def Solve(self,A,B):
        m=len(A)
        n=len(A[0])
        mod = A[0][0]%B
        d=[]
        for i in range(m):
            for j in range(n):
                if A[i][j]%B != mod:
                    return -1
                d.append(A[i][j]//B)
        d.sort()
        mid = (n*m) >> 1
        ans = 0
        for i in d:
            ans += abs(i-d[mid])

        if (n*m)%2==0:
            mid -= 1
            ans2=0
            for i in d:
                ans2 += abs(i-d[mid])
            ans = min(ans,ans2)
        return ans


if __name__ == '__main__':
    A=[[0,2,8],
       [8,2,0],
       [0,2,8]]
    B=2
    C=Solution()
    print(C.Solve(A,B))
