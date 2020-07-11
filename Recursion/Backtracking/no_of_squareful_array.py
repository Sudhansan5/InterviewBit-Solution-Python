from collections import Counter
class Solution:
    def dfs(self,A,n):
        self.count[A] -= 1
        global ans
        if n == 0:
            ans = 1
        else:
            ans = 0
            for y in self.graph[A]:
                if self.count[y]:
                    ans += self.dfs(A, n-1)
        self.count[A] += 1
        return ans

    def Solve(self,A):
        self.count = Counter(A)
        self.graph = {x: [] for x in self.count}
        for x in self.count:
            for y in self.count:
                if int((x+y)**.5 + 0.5) ** 2 == x+y:
                    self.graph[x].append(y)

        return sum(self.dfs(x, len(A)-1) for x in self.count)

if __name__ == '__main__':
    A = [2,2,2]
    B = Solution()
    print(B.Solve(A))
