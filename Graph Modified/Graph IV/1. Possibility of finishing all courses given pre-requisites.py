from collections import deque, defaultdict


class Solution:
    def Solve(self, A, B, C):
        graph = defaultdict(list)
        inDegree = {}
        q = deque()

        for i in range(A):
            inDegree[i] = 0

        for i, j in zip(B, C):
            graph[i - 1].append(j - 1)

        for i in graph:
            for j in graph[i]:
                if j not in inDegree:
                    inDegree[j] = 1
                else:
                    inDegree[j] += 1

        for i in inDegree:
            if inDegree[i] == 0:
                q.append(i)
        ans = []
        while q:
            i = q.popleft()
            ans.append(i)

            for j in graph[i]:
                inDegree[j] -= 1
                if inDegree[j] == 0:
                    q.append(j)

        return 1 if len(ans) == A else 0


if __name__ == '__main__':
    A = 5
    B = [1, 3, 4, 5]
    C = [2, 1, 5, 3]
    D = Solution()
    print(D.Solve(A, B, C))
