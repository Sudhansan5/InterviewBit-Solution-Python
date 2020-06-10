class Solution:
    def Solve(self,A):
        n=len(A)
        pre=[0 for _ in range(n)]
        post=[0 for _ in range(n)]
        pre[0]=A[0]
        for i in range(1,n):
            if A[i] == 0:
                pre[i] = 0
            else:
                pre[i] = pre[i-1]+A[i]

        post[n-1] = A[n-1]
        for i in reversed(range(n-1)):
            if A[i] == 0:
                post[i] = 0
            else:
                post[i] = post[i+1] + A[i]
        ans = []
        for i in range(n-1):
            if A[i] == 0:
                ans.append(pre[i-1]+post[i+1])
        count = 0
        for i in range(n):
            if A[i] == 1:
                count+=1

        if count > max(ans):
            return max(ans)+1
        else:
            return max(ans)


if __name__ == '__main__':
    A=[1,1,1,0,1,1,1,0,1]
    B=Solution()
    print(B.Solve(A))
