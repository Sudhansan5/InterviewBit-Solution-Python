from collections import defaultdict, deque
class Solution:
    def Solve(self, A, B):
        graph = defaultdict(list)
        for i, j in B:
            graph[i].append(j)

        inDegree = {}
        q = deque()

        for i in range(A):
            inDegree[i] = 0

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

        return ans


if __name__ == '__main__':
    A = 4
    B = [[0, 1],
         [0, 2],
         [1, 3],
         [2, 1],
         [2, 3]]
    C = Solution()
    print(C.Solve(A, B))
