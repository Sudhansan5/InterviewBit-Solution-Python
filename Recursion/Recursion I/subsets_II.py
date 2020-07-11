class Solution:
    def __init__(self):
        self.ans = []

    def subsets(self,A,i,aux,p):
        if p:
            if aux not in self.ans:
                self.ans.append(aux)
        if i == len(A):
            return 1
        take = self.subsets(A, i+1, aux + [A[i]], True)
        dont = self.subsets(A, i+1, aux, False)
        return take + dont

    def Solve(self,A):
        self.subsets(A, 0, [], True)
        return self.ans

if __name__ == '__main__':
    A = [1, 2, 2]
    B = Solution()
    print(B.Solve(A))
