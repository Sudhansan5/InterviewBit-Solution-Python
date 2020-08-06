from collections import deque
class Solution:
    def histogram(self,A):
        n = len(A)
        stack = deque()
        max_area = 0
        i = 0
        while i < n:
            if not stack or A[stack[-1]] <= A[i]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                area = A[top] * ((i - stack[-1] - 1) if stack else i)
                max_area = max(max_area,area)

        while stack:
            top = stack.pop()
            area = A[top] * ((i-stack[-1] - 1) if stack else i)
            max_area = max(max_area,area)

        return max_area

    def Solve(self, A):
        m = len(A)
        n = len(A[0])
        dp = A[0]
        ans = 0

        area = self.histogram(dp)
        ans = max(ans, area)

        for i in range(1,m):
            for j in range(n):
                if A[i][j] == 1:
                    dp[j] += 1
                else:
                    dp[j] = 0
            area = self.histogram(dp)
            ans = max(ans, area)

        return ans

if __name__ == '__main__':
    A = [[1, 1, 1],
         [0, 1, 1],
         [1, 0, 0]]

    B = Solution()
    print(B.Solve(A))
