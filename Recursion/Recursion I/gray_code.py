class Solution:
    def Solve(self,A):
        ans = []
        for i in range(2**A):
            ans.append((i>>1)^i)
        return ans

if __name__ == '__main__':
    A = 2
    B = Solution()
    print(B.Solve(A))
