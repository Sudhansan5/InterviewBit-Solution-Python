class Solution:
    def Solve(self,A):
        n=len(A)
        if n <= 1 and A[0] == 0:
            return 0
        if n > 1 and A[0] == 0:
            return -1
        max_reach = A[0]
        steps = A[0]
        jump = 1
        for i in range(1,n):
            if i == n-1:
                return jump
            max_reach = max(max_reach, A[i]+i)
            steps -= 1
            if steps == 0:
                jump += 1
                if i > max_reach:
                    return -1
                steps = max_reach - i
        return -1

A=[2,3,1,1,4]
B=Solution()
print(B.Solve(A))
