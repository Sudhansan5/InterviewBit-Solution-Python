class Solution:
    def dp(self,A,aux):
        global ans
        if aux[A] != 0:
            return aux[A]
        if A <= 2:
            ans = A
        else:
            ans = self.dp(A-1,aux) + self.dp(A-2,aux)
        aux[A] = ans
        return ans

    def Solve(self,A):
        aux=[0]*(A+1)
        self.dp(A,aux)
        return aux[A]

A=5
B=Solution()
print(B.Solve(A))
