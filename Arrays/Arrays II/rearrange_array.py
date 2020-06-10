class Solution:
    def Solve(self,A):  #Space = O(n)
        n=len(A)
        ans=[0 for _ in range(n)]
        for i in range(n):
            ans[A[i]] = i
        return ans

    def rearrange(self,A,n,i): #Space O(1)
        val = -(i+1)
        i = A[i] - 1
        while A[i] > 0:
            tmp = A[i]-1
            A[i] = val
            val = -(i+1)
            i = tmp

    def solve(self,A):
        n=len(A)
        for i in range(n):
            A[i] += 1

        for i in range(n):
            if A[i] > 0:
                self.rearrange(A,n,i)

        for i in range(n):
            A[i] = (-A[i]) - 1
        return A

if __name__ == '__main__':
    A=[1,2,3,4,0]
    B=Solution()
    print(B.Solve(A))
    print(B.solve(A))
