class Solution:
    def Solve(self, A):
        n = len(A)
        min_price = float('inf')
        max_profit = 0

        for i in range(n):
            min_price = min(min_price,A[i])
            max_profit = max(max_profit,A[i] - min_price)

        return max_profit

if __name__ == '__main__':
    A = [1, 4, 5, 2, 4]
    B = Solution()
    print(B.Solve(A))
