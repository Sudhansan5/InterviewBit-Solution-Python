class Solution:
    def __init__(self):
        self.ans = []

    def find_perm(self,A,index, aux):
        if index == len(A):
            self.ans.append(aux)
            return
        for i in range(index, len(A)):
            flag = 0
            for j in range(index,i):
                if A[i] == A[j]:
                    flag = 1
            if flag == 1:
                continue
            A[i], A[index] = A[index], A[i]
            self.find_perm(A, index + 1, aux + [A[index]])
            A[i], A[index] = A[index], A[i]

    def Solve(self,A):
        self.find_perm(A,0, [])
        return self.ans

if __name__ == '__main__':
    A = [1,2,3]
    B = Solution()
    print(B.Solve(A))
