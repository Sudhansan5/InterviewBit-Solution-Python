from collections import defaultdict, deque


class Solution:
    def dfs(self,B, v, parent, vis, aux):
        aux[v] = B[v]
        for node in self.graph[v]:
            if node != parent:
                self.dfs(B, node, v, vis, aux)
                aux[v] ^= aux[node]

    def Solve(self, A, B, C):
        self.graph = defaultdict(list)
        for i, j in C:
            self.graph[i].append(j)
            self.graph[j].append(i)

        vis = [False for _ in range(A)]
        aux = [0 for _ in range(A)]
        self.dfs(B,0,-1,vis, aux)
        max_xor = -1
        max_xor_cnt = 0

        for i in range(A):
            if max_xor < aux[i]:
                max_xor = aux[i]
                max_xor_cnt = 1
            elif max_xor == aux[i]:
                max_xor_cnt += 1

        return [max_xor,max_xor_cnt], aux


if __name__ == '__main__':
    A = 5
    B = [11, 10, 12, 12, 7]
    C = [[0, 4],
         [1, 0],
         [1, 3],
         [3, 2]]
    D = Solution()
    print(D.Solve(A, B, C))
