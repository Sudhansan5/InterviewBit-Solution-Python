class Solution:
    def __init__(self):
        self.ans =[]
    def subset(self,A,i,n,aux, p):
        if p: self.ans.append(aux)
        if i == n:
            return 1
        take = self.subset(A,i+1,n, aux + [A[i]], True)
        dont = self.subset(A, i+1, n, aux, False)
        return take + dont
    def Solve(self,A):
        A.sort()
        self.subset(A, 0, len(A), [], True)
        return self.ans


if __name__ == '__main__':
    A = [1, 2, 3]
    B = Solution()
    print(B.Solve(A))
