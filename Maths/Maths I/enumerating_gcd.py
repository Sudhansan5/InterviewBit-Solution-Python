class Solution:
    def Solve(self,A,B):
        if len(A) == len(B):
            return A if A == B else '1'
        else:
            if len(A) < len(B):
                B,A=A,B
            if A[:len(B)] == B:
                return self.Solve(A[len(B):],B)
            else:
                return '1'

if __name__ == '__main__':
    A='100'
    B='10000'
    C=Solution()
    print(C.Solve(A,B))
