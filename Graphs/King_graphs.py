class Solution:
    def Solve(self,A):
        m=len(A)
        for k in range(m):
            for i in range(m):
                for j in range(m):
                    if A[i][j]==-1:
                        A[i][j]=float('inf')
                    A[i][j]=min(A[i][j],A[i][k]+A[k][j])
        ans=-1
        max_min_dis=float('inf')
        for i in range(m):
            max_dis=float('-inf')
            for j in range(m):
                max_dis = max(max_dis,A[i][j])
            if max_dis < max_min_dis:
                max_min_dis=max_dis
                ans=i

        return ans

A=[[0, 6, 8,-1],
   [6, 0, 9 -1],
   [8, 9, 0, 4],
   [-1,-1, 4,0]]

C=[[0, 8, 8,-1],
   [8, 0, 4,-1],
   [8, 4, 0, 1],
   [-1,-1,1, 0]]

D=[[0,-1, 9,-1,-1],
   [-1,0, 5,-1,-1],
   [9, 5, 0, 3,-1],
   [-1,-1,3, 0, 9],
   [-1,-1,-1,9, 0]]

B=Solution()
print(B.Solve(D))
